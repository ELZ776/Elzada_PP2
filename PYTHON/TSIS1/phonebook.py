import csv
import json

import psycopg2

from connect import get_connection


def run_procedures_file():
    """Create procedures and functions from procedures.sql."""

    conn = get_connection()
    cur = conn.cursor()

    try:
        with open(
            "procedures.sql",
            "r",
            encoding="utf-8"
        ) as file:
            sql_code = file.read()

        cur.execute(sql_code)
        conn.commit()

        print(
            "Procedures and functions created successfully."
        )

    except (OSError, psycopg2.Error) as error:
        conn.rollback()
        print("Setup error:", error)

    finally:
        cur.close()
        conn.close()


def get_group_id(cur, group_name):
    """Return group ID and create the group if needed."""

    group_name = group_name.strip() or "Other"

    cur.execute(
        """
        INSERT INTO groups (name)
        VALUES (%s)
        ON CONFLICT (name) DO NOTHING;
        """,
        (group_name,)
    )

    cur.execute(
        """
        SELECT id
        FROM groups
        WHERE name = %s;
        """,
        (group_name,)
    )

    return cur.fetchone()[0]


def print_contacts(rows):
    """Print contacts in console."""

    if not rows:
        print("No contacts found.")
        return

    print(
        "\nID | Name | Surname | Email | "
        "Birthday | Group | Phones"
    )
    print("-" * 110)

    for row in rows:
        values = [
            "" if value is None else str(value)
            for value in row
        ]

        print(" | ".join(values))


def show_all_contacts():
    """Show all contacts with group and phones."""

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            SELECT
                c.id,
                c.username,
                c.surname,
                c.email,
                c.birthday,
                g.name,
                COALESCE(
                    string_agg(
                        DISTINCT
                        p.phone || ' (' || p.type || ')',
                        ', '
                    ),
                    ''
                ) AS phones

            FROM contacts c

            LEFT JOIN groups g
                ON c.group_id = g.id

            LEFT JOIN phones p
                ON c.id = p.contact_id

            GROUP BY
                c.id,
                c.username,
                c.surname,
                c.email,
                c.birthday,
                g.name

            ORDER BY c.id;
            """
        )

        print_contacts(cur.fetchall())

    except psycopg2.Error as error:
        print("Show error:", error)

    finally:
        cur.close()
        conn.close()


def filter_by_group():
    """Show contacts from one group."""

    group_name = input(
        "Enter group name: "
    ).strip()

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            SELECT
                c.id,
                c.username,
                c.surname,
                c.email,
                c.birthday,
                g.name,
                COALESCE(
                    string_agg(
                        DISTINCT
                        p.phone || ' (' || p.type || ')',
                        ', '
                    ),
                    ''
                ) AS phones

            FROM contacts c

            LEFT JOIN groups g
                ON c.group_id = g.id

            LEFT JOIN phones p
                ON c.id = p.contact_id

            WHERE g.name ILIKE %s

            GROUP BY
                c.id,
                c.username,
                c.surname,
                c.email,
                c.birthday,
                g.name

            ORDER BY c.username;
            """,
            (group_name,)
        )

        print_contacts(cur.fetchall())

    except psycopg2.Error as error:
        print("Filter error:", error)

    finally:
        cur.close()
        conn.close()


def search_by_email():
    """Search contacts by part of email."""

    email_part = input(
        "Enter email pattern: "
    ).strip()

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            SELECT
                c.id,
                c.username,
                c.surname,
                c.email,
                c.birthday,
                g.name,
                COALESCE(
                    string_agg(
                        DISTINCT
                        p.phone || ' (' || p.type || ')',
                        ', '
                    ),
                    ''
                ) AS phones

            FROM contacts c

            LEFT JOIN groups g
                ON c.group_id = g.id

            LEFT JOIN phones p
                ON c.id = p.contact_id

            WHERE c.email ILIKE %s

            GROUP BY
                c.id,
                c.username,
                c.surname,
                c.email,
                c.birthday,
                g.name

            ORDER BY c.username;
            """,
            (f"%{email_part}%",)
        )

        print_contacts(cur.fetchall())

    except psycopg2.Error as error:
        print("Email search error:", error)

    finally:
        cur.close()
        conn.close()


def sort_contacts():
    """Sort contacts by name, birthday, or date added."""

    print("1. Sort by name")
    print("2. Sort by birthday")
    print("3. Sort by date added")

    choice = input(
        "Choose sorting: "
    ).strip()

    sort_columns = {
        "1": "c.username",
        "2": "c.birthday",
        "3": "c.created_at"
    }

    column = sort_columns.get(choice)

    if column is None:
        print("Invalid sorting option.")
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        query = f"""
            SELECT
                c.id,
                c.username,
                c.surname,
                c.email,
                c.birthday,
                g.name,
                COALESCE(
                    string_agg(
                        DISTINCT
                        p.phone || ' (' || p.type || ')',
                        ', '
                    ),
                    ''
                ) AS phones

            FROM contacts c

            LEFT JOIN groups g
                ON c.group_id = g.id

            LEFT JOIN phones p
                ON c.id = p.contact_id

            GROUP BY
                c.id,
                c.username,
                c.surname,
                c.email,
                c.birthday,
                g.name,
                c.created_at

            ORDER BY {column} NULLS LAST;
        """

        cur.execute(query)
        print_contacts(cur.fetchall())

    except psycopg2.Error as error:
        print("Sort error:", error)

    finally:
        cur.close()
        conn.close()


def paginated_navigation():
    """Navigate through contacts page by page."""

    page_size = 3
    offset = 0

    conn = get_connection()
    cur = conn.cursor()

    try:
        while True:
            cur.execute(
                """
                SELECT
                    c.id,
                    c.username,
                    c.surname,
                    c.email,
                    c.birthday,
                    g.name,
                    COALESCE(
                        string_agg(
                            DISTINCT
                            p.phone || ' (' || p.type || ')',
                            ', '
                        ),
                        ''
                    ) AS phones

                FROM contacts c

                LEFT JOIN groups g
                    ON c.group_id = g.id

                LEFT JOIN phones p
                    ON c.id = p.contact_id

                GROUP BY
                    c.id,
                    c.username,
                    c.surname,
                    c.email,
                    c.birthday,
                    g.name

                ORDER BY c.id

                LIMIT %s
                OFFSET %s;
                """,
                (page_size, offset)
            )

            rows = cur.fetchall()

            print(
                f"\nPage {offset // page_size + 1}"
            )

            print_contacts(rows)

            command = input(
                "\nn = next, p = previous, q = quit: "
            ).strip().lower()

            if command == "n":
                if len(rows) < page_size:
                    print("This is the last page.")
                else:
                    offset += page_size

            elif command == "p":
                offset = max(
                    0,
                    offset - page_size
                )

            elif command == "q":
                break

            else:
                print("Invalid command.")

    except psycopg2.Error as error:
        print("Pagination error:", error)

    finally:
        cur.close()
        conn.close()


def import_extended_csv():
    """Import contacts from contacts.csv."""

    filename = input(
        "CSV filename [contacts.csv]: "
    ).strip()

    if not filename:
        filename = "contacts.csv"

    conn = get_connection()
    cur = conn.cursor()

    try:
        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                username = row["username"].strip()
                surname = row["surname"].strip()
                email = row["email"].strip()
                birthday = row["birthday"].strip()
                group_name = row["group"].strip()
                phone = row["phone"].strip()
                phone_type = (
                    row["phone_type"]
                    .strip()
                    .lower()
                )

                if not username:
                    print("Skipped empty username.")
                    continue

                if (
                    not phone.isdigit()
                    or len(phone) < 10
                    or len(phone) > 15
                ):
                    print(
                        f"Skipped invalid phone: {phone}"
                    )
                    continue

                if phone_type not in {
                    "home",
                    "work",
                    "mobile"
                }:
                    print(
                        f"Skipped invalid type: {phone_type}"
                    )
                    continue

                group_id = get_group_id(
                    cur,
                    group_name
                )

                cur.execute(
                    """
                    INSERT INTO contacts (
                        username,
                        surname,
                        email,
                        birthday,
                        group_id
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )

                    ON CONFLICT (username)
                    DO UPDATE SET
                        surname = EXCLUDED.surname,
                        email = EXCLUDED.email,
                        birthday = EXCLUDED.birthday,
                        group_id = EXCLUDED.group_id

                    RETURNING id;
                    """,
                    (
                        username,
                        surname or None,
                        email or None,
                        birthday or None,
                        group_id
                    )
                )

                contact_id = cur.fetchone()[0]

                cur.execute(
                    """
                    INSERT INTO phones (
                        contact_id,
                        phone,
                        type
                    )
                    VALUES (
                        %s,
                        %s,
                        %s
                    )

                    ON CONFLICT (
                        contact_id,
                        phone
                    )
                    DO UPDATE SET
                        type = EXCLUDED.type;
                    """,
                    (
                        contact_id,
                        phone,
                        phone_type
                    )
                )

        conn.commit()
        print("CSV import completed successfully.")

    except (
        OSError,
        KeyError,
        psycopg2.Error
    ) as error:

        conn.rollback()
        print("CSV import error:", error)

    finally:
        cur.close()
        conn.close()


def export_to_json():
    """Export all contacts to JSON."""

    filename = input(
        "JSON filename [contacts_export.json]: "
    ).strip()

    if not filename:
        filename = "contacts_export.json"

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            SELECT
                c.id,
                c.username,
                c.surname,
                c.email,
                c.birthday,
                g.name

            FROM contacts c

            LEFT JOIN groups g
                ON c.group_id = g.id

            ORDER BY c.id;
            """
        )

        result = []

        for contact in cur.fetchall():
            contact_id = contact[0]

            cur.execute(
                """
                SELECT phone, type
                FROM phones
                WHERE contact_id = %s
                ORDER BY id;
                """,
                (contact_id,)
            )

            phone_list = []

            for phone, phone_type in cur.fetchall():
                phone_list.append(
                    {
                        "phone": phone,
                        "type": phone_type
                    }
                )

            result.append(
                {
                    "username": contact[1],
                    "surname": contact[2],
                    "email": contact[3],
                    "birthday": (
                        contact[4].isoformat()
                        if contact[4]
                        else None
                    ),
                    "group": contact[5],
                    "phones": phone_list
                }
            )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                result,
                file,
                ensure_ascii=False,
                indent=4
            )

        print(
            f"Contacts exported to {filename}."
        )

    except (
        OSError,
        psycopg2.Error
    ) as error:

        print("JSON export error:", error)

    finally:
        cur.close()
        conn.close()


def import_from_json():
    """Import contacts from JSON."""

    filename = input(
        "Enter JSON filename: "
    ).strip()

    try:
        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            contacts = json.load(file)

    except (
        OSError,
        json.JSONDecodeError
    ) as error:

        print("JSON read error:", error)
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        for contact in contacts:
            username = contact["username"].strip()

            cur.execute(
                """
                SELECT id
                FROM contacts
                WHERE username = %s;
                """,
                (username,)
            )

            existing = cur.fetchone()

            if existing:
                choice = input(
                    f"{username} exists. "
                    "s = skip, o = overwrite: "
                ).strip().lower()

                if choice != "o":
                    continue

                contact_id = existing[0]

                cur.execute(
                    """
                    DELETE FROM phones
                    WHERE contact_id = %s;
                    """,
                    (contact_id,)
                )

                group_id = get_group_id(
                    cur,
                    contact.get("group", "Other")
                )

                cur.execute(
                    """
                    UPDATE contacts
                    SET surname = %s,
                        email = %s,
                        birthday = %s,
                        group_id = %s
                    WHERE id = %s;
                    """,
                    (
                        contact.get("surname"),
                        contact.get("email"),
                        contact.get("birthday"),
                        group_id,
                        contact_id
                    )
                )

            else:
                group_id = get_group_id(
                    cur,
                    contact.get("group", "Other")
                )

                cur.execute(
                    """
                    INSERT INTO contacts (
                        username,
                        surname,
                        email,
                        birthday,
                        group_id
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    RETURNING id;
                    """,
                    (
                        username,
                        contact.get("surname"),
                        contact.get("email"),
                        contact.get("birthday"),
                        group_id
                    )
                )

                contact_id = cur.fetchone()[0]

            for phone_data in contact.get(
                "phones",
                []
            ):
                cur.execute(
                    """
                    INSERT INTO phones (
                        contact_id,
                        phone,
                        type
                    )
                    VALUES (%s, %s, %s)

                    ON CONFLICT (
                        contact_id,
                        phone
                    )
                    DO UPDATE SET
                        type = EXCLUDED.type;
                    """,
                    (
                        contact_id,
                        phone_data["phone"],
                        phone_data["type"]
                    )
                )

        conn.commit()
        print("JSON import completed.")

    except (
        KeyError,
        psycopg2.Error
    ) as error:

        conn.rollback()
        print("JSON import error:", error)

    finally:
        cur.close()
        conn.close()


def add_phone():
    """Call add_phone procedure."""

    username = input(
        "Contact name: "
    ).strip()

    phone = input(
        "New phone: "
    ).strip()

    phone_type = input(
        "Type (home/work/mobile): "
    ).strip().lower()

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            CALL add_phone(%s, %s, %s);
            """,
            (
                username,
                phone,
                phone_type
            )
        )

        conn.commit()
        print("Phone added successfully.")

    except psycopg2.Error as error:
        conn.rollback()
        print("Add phone error:", error)

    finally:
        cur.close()
        conn.close()


def move_to_group():
    """Call move_to_group procedure."""

    username = input(
        "Contact name: "
    ).strip()

    group_name = input(
        "New group: "
    ).strip()

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            CALL move_to_group(%s, %s);
            """,
            (
                username,
                group_name
            )
        )

        conn.commit()
        print("Contact moved successfully.")

    except psycopg2.Error as error:
        conn.rollback()
        print("Move error:", error)

    finally:
        cur.close()
        conn.close()


def advanced_search():
    """Call search_contacts function."""

    query = input(
        "Enter search query: "
    ).strip()

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            SELECT *
            FROM search_contacts(%s);
            """,
            (query,)
        )

        print_contacts(cur.fetchall())

    except psycopg2.Error as error:
        print("Search error:", error)

    finally:
        cur.close()
        conn.close()


def menu():
    while True:
        print("\nTSIS 1 EXTENDED PHONEBOOK")
        print("1. Create procedures/functions")
        print("2. Import extended CSV")
        print("3. Show all contacts")
        print("4. Filter by group")
        print("5. Search by email")
        print("6. Sort contacts")
        print("7. Pagination")
        print("8. Export to JSON")
        print("9. Import from JSON")
        print("10. Add phone")
        print("11. Move contact to group")
        print("12. Advanced search")
        print("0. Exit")

        choice = input(
            "Choose option: "
        ).strip()

        if choice == "1":
            run_procedures_file()

        elif choice == "2":
            import_extended_csv()

        elif choice == "3":
            show_all_contacts()

        elif choice == "4":
            filter_by_group()

        elif choice == "5":
            search_by_email()

        elif choice == "6":
            sort_contacts()

        elif choice == "7":
            paginated_navigation()

        elif choice == "8":
            export_to_json()

        elif choice == "9":
            import_from_json()

        elif choice == "10":
            add_phone()

        elif choice == "11":
            move_to_group()

        elif choice == "12":
            advanced_search()

        elif choice == "0":
            print("Program finished.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()