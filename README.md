# My PhoneBook v2.0

A simple command-line phone book application written in **Python**. It uses **SQLite** to save contacts locally, so your contacts remain available after you close the program.

## Features

- **Add Contact** — save a contact's name and phone number.
- **List Contacts** — display all saved contacts.
- **Search Contact** — find a contact by name or phone number.
- **Delete Contact** — delete contacts by name or phone number.
- **Edit Contact** — update a contact's phone number using their name.
- **Local Database** — stores data in a `phonebook.db` file.

## Requirements

- Python 3
- No third-party packages are required. The project uses Python's built-in `sqlite3` and `os` modules.

## Run the project

1. Clone this repository or download the source code.
2. Open a terminal in the project folder.
3. Run:

```bash
python phonebook.py
```

On some systems, use:

```bash
python3 phonebook.py
```

The application creates `phonebook.db` automatically in the working directory the first time it runs.

## Menu

When the program starts, choose an option:

| Option | Action |
| --- | --- |
| 1 | Add Contact |
| 2 | List Contact |
| 3 | Search Contact |
| 4 | Delete Contact |
| 5 | Edit Contact |
| 6 | Exit |

## Project files

```text
MyPhonebook/
├── phonebook.py
└── phonebook.db   # created automatically when you run the app
```

## Notes

- Contacts are stored locally on the computer; this project does not sync them online.
- Keep the `phonebook.db` file if you want to keep your saved contacts.
- Searching and editing use the contact name or number entered in the program. If multiple contacts share the same name, editing by name can affect more than one matching record.

## License

No license has been specified yet.
