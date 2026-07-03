CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    surname VARCHAR(100),
    phone VARCHAR(30) UNIQUE NOT NULL
);

ALTER TABLE phonebook
ADD COLUMN IF NOT EXISTS surname VARCHAR(100);


CREATE OR REPLACE FUNCTION search_phonebook(p_pattern TEXT)
RETURNS TABLE (
    id INTEGER,
    username VARCHAR,
    surname VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.surname, p.phone
    FROM phonebook p
    WHERE p.username ILIKE '%' || p_pattern || '%'
       OR p.surname ILIKE '%' || p_pattern || '%'
       OR p.phone ILIKE '%' || p_pattern || '%'
    ORDER BY p.id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_phonebook_page(p_limit INTEGER, p_offset INTEGER)
RETURNS TABLE (
    id INTEGER,
    username VARCHAR,
    surname VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.surname, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;