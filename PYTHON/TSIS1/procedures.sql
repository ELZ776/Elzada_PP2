-- 1. Add a new phone number to an existing contact

CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INTEGER;
BEGIN
    IF p_type NOT IN ('home', 'work', 'mobile') THEN
        RAISE EXCEPTION
            'Invalid phone type. Use home, work, or mobile.';
    END IF;

    IF p_phone !~ '^[0-9]{10,15}$' THEN
        RAISE EXCEPTION
            'Invalid phone number. Use 10 to 15 digits.';
    END IF;

    SELECT id
    INTO v_contact_id
    FROM contacts
    WHERE username = p_contact_name;

    IF v_contact_id IS NULL THEN
        RAISE EXCEPTION
            'Contact % does not exist.',
            p_contact_name;
    END IF;

    INSERT INTO phones (
        contact_id,
        phone,
        type
    )
    VALUES (
        v_contact_id,
        p_phone,
        p_type
    )
    ON CONFLICT (contact_id, phone)
    DO UPDATE SET type = EXCLUDED.type;
END;
$$;


-- 2. Move a contact to another group.
-- If the group does not exist, create it.

CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_group_id INTEGER;
BEGIN
    IF p_group_name IS NULL
       OR trim(p_group_name) = '' THEN
        RAISE EXCEPTION
            'Group name cannot be empty.';
    END IF;

    INSERT INTO groups (name)
    VALUES (trim(p_group_name))
    ON CONFLICT (name) DO NOTHING;

    SELECT id
    INTO v_group_id
    FROM groups
    WHERE name = trim(p_group_name);

    UPDATE contacts
    SET group_id = v_group_id
    WHERE username = p_contact_name;

    IF NOT FOUND THEN
        RAISE EXCEPTION
            'Contact % does not exist.',
            p_contact_name;
    END IF;
END;
$$;


-- 3. Search by name, surname, email, or phone

CREATE OR REPLACE FUNCTION search_contacts(
    p_query TEXT
)
RETURNS TABLE (
    id INTEGER,
    username VARCHAR,
    surname VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR,
    phone_numbers TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY

    SELECT
        c.id,
        c.username,
        c.surname,
        c.email,
        c.birthday,
        g.name,
        COALESCE(
            string_agg(
                DISTINCT p.phone || ' (' || p.type || ')',
                ', '
            ),
            ''
        ) AS phone_numbers

    FROM contacts c

    LEFT JOIN groups g
        ON c.group_id = g.id

    LEFT JOIN phones p
        ON c.id = p.contact_id

    WHERE c.username ILIKE '%' || p_query || '%'
       OR COALESCE(c.surname, '')
            ILIKE '%' || p_query || '%'
       OR COALESCE(c.email, '')
            ILIKE '%' || p_query || '%'
       OR EXISTS (
            SELECT 1
            FROM phones p2
            WHERE p2.contact_id = c.id
              AND p2.phone
                    ILIKE '%' || p_query || '%'
       )

    GROUP BY
        c.id,
        c.username,
        c.surname,
        c.email,
        c.birthday,
        g.name

    ORDER BY c.username;
END;
$$;