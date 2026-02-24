# CRM Contact Manager

A CLI-based CRM Contact Manager built with **Python** and **SQLite** to simulate core CRM functionality — including contact management, SQL database operations, and CSV reporting.

Inspired by enterprise CRM platforms like **Microsoft Dynamics 365**.

---

## Features

- ➕ Add new contacts (name, email, phone, company)
- 📋 View all contacts stored in the database
- 🔍 Search contacts by name or company
- 🗑️ Delete contacts by email
- 📤 Export all contacts to CSV for reporting
- ⚠️ Duplicate email detection and graceful error handling

---

## Tech Stack

- Python 3.x
- SQLite3 (built-in Python library)
- CSV module (built-in Python library)
- OOP design — `Contact` class, `Database` class

---

## Project Structure

```
crm-contact-manager/
│
├── main.py         # Entry point — CLI menu and user interaction
├── database.py     # Database class — all SQL operations (CRUD)
├── contact.py      # Contact class — OOP model
└── README.md
```

---

## Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/abdxlRafay/crm-contact-manager.git
cd crm-contact-manager
```

**2. Run the program**
```bash
python main.py
```

No external libraries required — uses Python built-ins only.

---

## How It Works

```
========================================
       CRM Contact Manager
========================================

1. Add Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Export to CSV
6. Exit
----------------------------------------
Select an option (1-6):
```

Contacts are stored persistently in a local SQLite database (`crm.db`). Each session loads existing data automatically.

---

## OOP Design

| Class | Responsibility |
|-------|---------------|
| `Contact` | Represents a single contact entity with attributes: name, email, phone, company |
| `Database` | Manages SQLite connection, table creation, and all CRUD operations |

---

## Author

**Abdul Rafay** — [GitHub](https://github.com/abdxlRafay)
