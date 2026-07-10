-- 1. Groups table
CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);


-- 2. Add default groups
INSERT INTO groups (name)
VALUES
    ('Family'),
    ('Work'),
    ('Friend'),
    ('Other')
ON CONFLICT (name) DO NOTHING;


-- 3. Rename old phonebook table to contacts
DO $$
BEGIN
    IF to_regclass('public.phonebook') IS NOT NULL
       AND to_regclass('public.contacts') IS NULL THEN

        ALTER TABLE phonebook RENAME TO contacts;

    END IF;
END;
$$;


-- 4. Create contacts table if it does not exist
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL
);


-- 5. Add new contact fields
ALTER TABLE contacts
ADD COLUMN IF NOT EXISTS surname VARCHAR(100),
ADD COLUMN IF NOT EXISTS email VARCHAR(100),
ADD COLUMN IF NOT EXISTS birthday DATE,
ADD COLUMN IF NOT EXISTS group_id INTEGER REFERENCES groups(id),
ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;


-- 6. Create phones table
CREATE TABLE IF NOT EXISTS phones (
    id SERIAL PRIMARY KEY,

    contact_id INTEGER NOT NULL
        REFERENCES contacts(id)
        ON DELETE CASCADE,

    phone VARCHAR(20) NOT NULL,

    type VARCHAR(10) NOT NULL
        CHECK (type IN ('home', 'work', 'mobile')),

    UNIQUE (contact_id, phone)
);


-- 7. Move old phone numbers to phones table
DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.columns
        WHERE table_name = 'contacts'
          AND column_name = 'phone'
    ) THEN

        INSERT INTO phones (contact_id, phone, type)
        SELECT id, phone, 'mobile'
        FROM contacts
        WHERE phone IS NOT NULL
          AND phone <> ''
        ON CONFLICT (contact_id, phone) DO NOTHING;

    END IF;
END;
$$;


-- 8. Put contacts without a group into Other
UPDATE contacts
SET group_id = (
    SELECT id
    FROM groups
    WHERE name = 'Other'
)
WHERE group_id IS NULL;