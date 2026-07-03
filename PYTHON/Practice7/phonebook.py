import csv
import psycopg2
from connect import get_connection


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(30) UNIQUE NOT NULL
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table phonebook is ready.")


def insert_contact(username, phone):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO phonebook (username, phone)
            VALUES (%s, %s);
        """, (username, phone))

        conn.commit()
        print("Contact inserted successfully.")

    except psycopg2.Error as error:
        conn.rollback()
        print("Insert error:", error)

    finally:
        cur.close()
        conn.close()


def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                username = row["username"]
                phone = row["phone"]

                try:
                    cur.execute("""
                        INSERT INTO phonebook (username, phone)
                        VALUES (%s, %s);
                    """, (username, phone))
                    conn.commit()

                except psycopg2.Error:
                    conn.rollback()
                    print(f"Skipped duplicate or invalid contact: {username}, {phone}")

        print("CSV import finished.")

    except FileNotFoundError:
        print("CSV file not found.")

    finally:
        cur.close()
        conn.close()


def show_all_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, username, phone
        FROM phonebook
        ORDER BY id;
    """)

    rows = cur.fetchall()

    if not rows:
        print("PhoneBook is empty.")
    else:
        print("\nID | Username | Phone")
        print("-" * 30)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]}")

    cur.close()
    conn.close()


def search_by_name(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, username, phone
        FROM phonebook
        WHERE username ILIKE %s
        ORDER BY id;
    """, (f"%{name}%",))

    rows = cur.fetchall()

    if not rows:
        print("No contacts found.")
    else:
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]}")

    cur.close()
    conn.close()


def search_by_phone_prefix(prefix):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, username, phone
        FROM phonebook
        WHERE phone LIKE %s
        ORDER BY id;
    """, (f"{prefix}%",))

    rows = cur.fetchall()

    if not rows:
        print("No contacts found.")
    else:
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]}")

    cur.close()
    conn.close()


def update_username(old_username, new_username):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            UPDATE phonebook
            SET username = %s
            WHERE username = %s;
        """, (new_username, old_username))

        conn.commit()

        if cur.rowcount == 0:
            print("Contact not found.")
        else:
            print("Username updated successfully.")

    except psycopg2.Error as error:
        conn.rollback()
        print("Update error:", error)

    finally:
        cur.close()
        conn.close()


def update_phone(username, new_phone):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            UPDATE phonebook
            SET phone = %s
            WHERE username = %s;
        """, (new_phone, username))

        conn.commit()

        if cur.rowcount == 0:
            print("Contact not found.")
        else:
            print("Phone updated successfully.")

    except psycopg2.Error as error:
        conn.rollback()
        print("Update error:", error)

    finally:
        cur.close()
        conn.close()


def delete_by_username(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM phonebook
        WHERE username = %s;
    """, (username,))

    conn.commit()

    if cur.rowcount == 0:
        print("Contact not found.")
    else:
        print("Contact deleted successfully.")

    cur.close()
    conn.close()


def delete_by_phone(phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM phonebook
        WHERE phone = %s;
    """, (phone,))

    conn.commit()

    if cur.rowcount == 0:
        print("Contact not found.")
    else:
        print("Contact deleted successfully.")

    cur.close()
    conn.close()


def menu():
    create_table()

    while True:
        print("\nPHONEBOOK MENU")
        print("1. Insert contact from console")
        print("2. Insert contacts from CSV")
        print("3. Show all contacts")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Update username")
        print("7. Update phone")
        print("8. Delete by username")
        print("9. Delete by phone")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            username = input("Enter username: ")
            phone = input("Enter phone: ")
            insert_contact(username, phone)

        elif choice == "2":
            filename = input("Enter CSV filename: ")
            insert_from_csv(filename)

        elif choice == "3":
            show_all_contacts()

        elif choice == "4":
            name = input("Enter name or part of name: ")
            search_by_name(name)

        elif choice == "5":
            prefix = input("Enter phone prefix: ")
            search_by_phone_prefix(prefix)

        elif choice == "6":
            old_username = input("Enter current username: ")
            new_username = input("Enter new username: ")
            update_username(old_username, new_username)

        elif choice == "7":
            username = input("Enter username: ")
            new_phone = input("Enter new phone: ")
            update_phone(username, new_phone)

        elif choice == "8":
            username = input("Enter username: ")
            delete_by_username(username)

        elif choice == "9":
            phone = input("Enter phone: ")
            delete_by_phone(phone)

        elif choice == "0":
            print("Program finished.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()