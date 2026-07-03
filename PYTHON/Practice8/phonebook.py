import json
import psycopg2
from connect import get_connection


def execute_sql_file(filename):
    conn = get_connection()
    cur = conn.cursor()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            sql = file.read()

        cur.execute(sql)
        conn.commit()
        print(f"{filename} executed successfully.")

    except Exception as error:
        conn.rollback()
        print("SQL file error:", error)

    finally:
        cur.close()
        conn.close()


def setup_database():
    execute_sql_file("functions.sql")
    execute_sql_file("procedures.sql")


def upsert_contact():
    username = input("Enter username: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "CALL upsert_contact(%s, %s, %s);",
            (username, surname, phone)
        )
        conn.commit()
        print("Contact inserted or updated successfully.")

    except psycopg2.Error as error:
        conn.rollback()
        print("Upsert error:", error)

    finally:
        cur.close()
        conn.close()


def insert_many_contacts():
    contacts = [
        {"username": "Aigerim", "surname": "Ali", "phone": "87011234567"},
        {"username": "Dias", "surname": "Omar", "phone": "87025556677"},
        {"username": "Elzada", "surname": "Zumabaikyzy", "phone": "87078889900"},
        {"username": "WrongUser", "surname": "Test", "phone": "abc123"},
        {"username": "", "surname": "NoName", "phone": "87070000000"}
    ]

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "CALL insert_many_contacts(%s::jsonb, %s::jsonb);",
            (json.dumps(contacts), None)
        )

        result = cur.fetchone()
        conn.commit()

        print("Bulk insert finished.")
        print("Incorrect data:")
        print(result[0])

    except psycopg2.Error as error:
        conn.rollback()
        print("Bulk insert error:", error)

    finally:
        cur.close()
        conn.close()


def search_contacts():
    pattern = input("Enter search pattern: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM search_phonebook(%s);",
        (pattern,)
    )

    rows = cur.fetchall()

    if not rows:
        print("No contacts found.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def show_page():
    limit = int(input("Enter LIMIT: "))
    offset = int(input("Enter OFFSET: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_phonebook_page(%s, %s);",
        (limit, offset)
    )

    rows = cur.fetchall()

    if not rows:
        print("No contacts found.")
    else:
        for row in rows:
            print(row)

    cur.close()
    conn.close()


def delete_contact():
    value = input("Enter username or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "CALL delete_contact(%s);",
            (value,)
        )
        conn.commit()
        print("Delete command executed.")

    except psycopg2.Error as error:
        conn.rollback()
        print("Delete error:", error)

    finally:
        cur.close()
        conn.close()


def show_all_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, username, surname, phone
        FROM phonebook
        ORDER BY id;
    """)

    rows = cur.fetchall()

    if not rows:
        print("PhoneBook is empty.")
    else:
        print("\nID | Username | Surname | Phone")
        print("-" * 45)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

    cur.close()
    conn.close()


def menu():
    while True:
        print("\nPRACTICE 8 PHONEBOOK MENU")
        print("1. Setup database functions and procedures")
        print("2. Insert/update one contact")
        print("3. Insert many contacts and show incorrect data")
        print("4. Search contacts by pattern")
        print("5. Show contacts with pagination")
        print("6. Delete contact by username or phone")
        print("7. Show all contacts")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            setup_database()

        elif choice == "2":
            upsert_contact()

        elif choice == "3":
            insert_many_contacts()

        elif choice == "4":
            search_contacts()

        elif choice == "5":
            show_page()

        elif choice == "6":
            delete_contact()

        elif choice == "7":
            show_all_contacts()

        elif choice == "0":
            print("Program finished.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()