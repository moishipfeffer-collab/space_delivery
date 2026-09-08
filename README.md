# Space Delivery Manager 🚀

This is a Python terminal project for managing space deliveries.

The user can register, login, and manage their own deliveries.

## What can you do?

* Register a new account
* Login
* Create a delivery
* See your deliveries
* Change delivery status
* Delete a delivery
* Logout

## Technologies

The project uses:

* Python
* MySQL
* Peewee
* PyMySQL
* bcrypt
* python-dotenv
* questionary

## Files

```text
main.py          - starts the program
app.py           - menus and application flow
db.py            - database connection
models.py        - User and Delivery models
auth.py          - register and login
deliveries.py    - delivery operations
```

## How to Run

First make sure MySQL is running and the database is set up.

Activate the virtual environment and install the packages:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

The program will open in the terminal and show the menu.

## Database

The project uses MySQL with Peewee ORM.

Each delivery belongs to the user who created it, so users can only manage their own deliveries.
