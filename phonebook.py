import os
import sqlite3

DB_NAME = "phonebook.db"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            number TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def add_contact(cur, conn):
    name = input("Enter Contact Name: ").strip()
    number = input("Enter Contact Number: ").strip()

    if not name or not number:
        print("Name and number cannot be empty.")
        return

    cur.execute(
        "INSERT INTO contacts (name, number) VALUES (?, ?)",
        (name, number)
    )
    conn.commit()
    print("Contact Added Successfully!")


def list_contacts(cur):
    cur.execute("SELECT id, name, number FROM contacts ORDER BY name")
    contacts = cur.fetchall()

    if not contacts:
        print("No contacts found!")
        return

    print("\n----- Contact List -----")
    for contact_id, name, number in contacts:
        print(f"ID: {contact_id} | Name: {name} | Number: {number}")


def find_contacts(cur, search_by, value):
    if search_by == "name":
        cur.execute(
            "SELECT id, name, number FROM contacts WHERE name LIKE ? ORDER BY name",
            (f"%{value}%",)
        )
    else:
        cur.execute(
            "SELECT id, name, number FROM contacts WHERE number LIKE ? ORDER BY name",
            (f"%{value}%",)
        )
    return cur.fetchall()


def search_contact(cur):
    choice = input("Search by Name or Number? (name/number): ").strip().lower()

    if choice not in ("name", "number"):
        print("Invalid Search Option!")
        return

    value = input(f"Enter Contact {choice.title()}: ").strip()
    contacts = find_contacts(cur, choice, value)

    if not contacts:
        print("Contact Not Found!")
        return

    for contact_id, name, number in contacts:
        print(f"ID: {contact_id} | Name: {name} | Number: {number}")


def delete_contact(cur, conn):
    choice = input("Delete by Name or Number? (name/number): ").strip().lower()

    if choice not in ("name", "number"):
        print("Invalid Search Option!")
        return

    value = input(f"Enter Contact {choice.title()}: ").strip()
    contacts = find_contacts(cur, choice, value)

    if not contacts:
        print("Contact Not Found!")
        return

    for contact_id, name, number in contacts:
        print(f"ID: {contact_id} | Name: {name} | Number: {number}")

    contact_id = input("Enter the ID of the contact to delete: ").strip()
    if not contact_id.isdigit():
        print("Invalid contact ID.")
        return

    cur.execute("DELETE FROM contacts WHERE id = ?", (int(contact_id),))
    conn.commit()

    if cur.rowcount:
        print("Contact Deleted!")
    else:
        print("Contact Not Found!")


def edit_contact(cur, conn):
    value = input("Enter Contact Name to Edit: ").strip()
    contacts = find_contacts(cur, "name", value)

    if not contacts:
        print("Contact Not Found!")
        return

    for contact_id, name, number in contacts:
        print(f"ID: {contact_id} | Name: {name} | Number: {number}")

    contact_id = input("Enter the ID of the contact to edit: ").strip()
    if not contact_id.isdigit():
        print("Invalid contact ID.")
        return

    cur.execute(
        "SELECT id, name, number FROM contacts WHERE id = ?",
        (int(contact_id),)
    )
    contact = cur.fetchone()

    if contact is None:
        print("Contact Not Found!")
        return

    new_name = input(f"Enter New Name [{contact[1]}]: ").strip()
    new_number = input(f"Enter New Number [{contact[2]}]: ").strip()

    new_name = new_name or contact[1]
    new_number = new_number or contact[2]

    cur.execute(
        "UPDATE contacts SET name = ?, number = ? WHERE id = ?",
        (new_name, new_number, int(contact_id))
    )
    conn.commit()
    print("Contact Updated!")


def main():
    conn = initialize_database()
    cur = conn.cursor()

    try:
        while True:
            input("\nPress Enter to continue...")
            clear_screen()

            print("\n----- My PhoneBook v2.0 -----")
            print("1. Add Contact")
            print("2. List Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Edit Contact")
            print("6. Exit")

            choice = input("\nChoose an option: ").strip()

            if choice == "1":
                add_contact(cur, conn)
            elif choice == "2":
                list_contacts(cur)
            elif choice == "3":
                search_contact(cur)
            elif choice == "4":
                delete_contact(cur, conn)
            elif choice == "5":
                edit_contact(cur, conn)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid Option!")

    finally:
        conn.close()


if __name__ == "__main__":
    main()
