from database import Database
from contact import Contact


def print_header():
    print("\n" + "=" * 40)
    print("       CRM Contact Manager")
    print("=" * 40)


def print_menu():
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Export to CSV")
    print("6. Exit")
    print("-" * 40)


def add_contact(db):
    print("\n--- Add New Contact ---")
    name = input("Name    : ").strip()
    email = input("Email   : ").strip()
    phone = input("Phone   : ").strip()
    company = input("Company : ").strip()

    if not name or not email:
        print("\n⚠️  Name and Email are required.")
        return

    contact = Contact(name, email, phone, company)
    db.add_contact(contact)


def view_contacts(db):
    print("\n--- All Contacts ---")
    contacts = db.get_all_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"\nContact #{i}")
        print(contact)
        print("-" * 30)


def search_contact(db):
    print("\n--- Search Contact ---")
    keyword = input("Enter name or company to search: ").strip()
    results = db.search_contact(keyword)
    if not results:
        print("No matching contacts found.")
        return
    for i, contact in enumerate(results, 1):
        print(f"\nResult #{i}")
        print(contact)
        print("-" * 30)


def delete_contact(db):
    print("\n--- Delete Contact ---")
    email = input("Enter email of contact to delete: ").strip()
    db.delete_contact(email)


def main():
    db = Database()
    print_header()

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            add_contact(db)
        elif choice == "2":
            view_contacts(db)
        elif choice == "3":
            search_contact(db)
        elif choice == "4":
            delete_contact(db)
        elif choice == "5":
            db.export_to_csv()
        elif choice == "6":
            print("\nGoodbye! 👋")
            db.close()
            break
        else:
            print("\n⚠️  Invalid option. Please select 1-6.")


if __name__ == "__main__":
    main()
