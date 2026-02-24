import sqlite3
import csv
from contact import Contact


class Database:
    """
    Handles all database operations — creating tables, adding,
    retrieving, searching, and deleting contacts using SQLite.
    """

    def __init__(self, db_name="crm.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                company TEXT
            )
        """)
        self.connection.commit()

    def add_contact(self, contact):
        try:
            self.cursor.execute("""
                INSERT INTO contacts (name, email, phone, company)
                VALUES (?, ?, ?, ?)
            """, (contact.name, contact.email, contact.phone, contact.company))
            self.connection.commit()
            print(f"\n✅ Contact '{contact.name}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"\n⚠️  A contact with email '{contact.email}' already exists.")

    def get_all_contacts(self):
        self.cursor.execute("SELECT name, email, phone, company FROM contacts")
        rows = self.cursor.fetchall()
        return [Contact(row[0], row[1], row[2], row[3]) for row in rows]

    def search_contact(self, keyword):
        self.cursor.execute("""
            SELECT name, email, phone, company FROM contacts
            WHERE name LIKE ? OR company LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))
        rows = self.cursor.fetchall()
        return [Contact(row[0], row[1], row[2], row[3]) for row in rows]

    def delete_contact(self, email):
        self.cursor.execute("DELETE FROM contacts WHERE email = ?", (email,))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print(f"\n✅ Contact with email '{email}' deleted successfully.")
        else:
            print(f"\n⚠️  No contact found with email '{email}'.")

    def export_to_csv(self, filename="contacts_export.csv"):
        contacts = self.get_all_contacts()
        if not contacts:
            print("\n⚠️  No contacts to export.")
            return
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Email", "Phone", "Company"])
            for c in contacts:
                writer.writerow([c.name, c.email, c.phone, c.company])
        print(f"\n✅ Contacts exported to '{filename}' successfully.")

    def close(self):
        self.connection.close()
