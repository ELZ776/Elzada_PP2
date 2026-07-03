CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    surname VARCHAR(100),
    phone VARCHAR(30) UNIQUE NOT NULL
);

ALTER TABLE phonebook
ADD COLUMN IF NOT EXISTS surname VARCHAR(100);


CREATE OR REPLACE PROCEDURE upsert_contact(
    p_username VARCHAR,
    p_surname VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_phone !~ '^[0-9]{10,15}$' THEN
        RAISE EXCEPTION 'Invalid phone number: %', p_phone;
    END IF;

    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_username) THEN
        UPDATE phonebook
        SET surname = p_surname,
            phone = p_phone
        WHERE username = p_username;
    ELSE
        INSERT INTO phonebook(username, surname, phone)
        VALUES (p_username, p_surname, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_contacts JSONB,
    INOUT p_invalid JSONB
)
LANGUAGE plpgsql
AS $$
DECLARE
    item JSONB;
    v_username VARCHAR;
    v_surname VARCHAR;
    v_phone VARCHAR;
    v_reason TEXT;
BEGIN
    p_invalid := '[]'::JSONB;

    FOR item IN SELECT * FROM jsonb_array_elements(p_contacts)
    LOOP
        v_username := item ->> 'username';
        v_surname := item ->> 'surname';
        v_phone := item ->> 'phone';
        v_reason := NULL;

        IF v_username IS NULL OR length(trim(v_username)) = 0 THEN
            v_reason := 'Username is empty';
        ELSIF v_phone IS NULL OR v_phone !~ '^[0-9]{10,15}$' THEN
            v_reason := 'Invalid phone number';
        END IF;

        IF v_reason IS NOT NULL THEN
            p_invalid := p_invalid || jsonb_build_array(
                item || jsonb_build_object('reason', v_reason)
            );
        ELSE
            IF EXISTS (SELECT 1 FROM phonebook WHERE username = v_username) THEN
                UPDATE phonebook
                SET surname = v_surname,
                    phone = v_phone
                WHERE username = v_username;
            ELSE
                INSERT INTO phonebook(username, surname, phone)
                VALUES (v_username, v_surname, v_phone);
            END IF;
        END IF;
    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p_value
       OR phone = p_value;
END;
$$;