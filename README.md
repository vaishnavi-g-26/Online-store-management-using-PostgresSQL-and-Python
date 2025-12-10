# Online-store-management-using-PostgresSQL-and-Python
📌 Project Description

The Online Store Management System is a Python-based application designed to manage store operations such as products, customers, and orders.
It uses PostgreSQL as the backend database and Python (Tkinter/CLI) as the interface to interact with the user.
The system helps stores maintain records, track customers, generate orders, and manage inventory efficiently.


📌 Features

•Add, update, delete, and view products

•Manage customers

•Create and view customer orders

•Track order status

•Store all data securely in PostgreSQL

•Simple Python-based GUI or command-line interface

•Extensible and easy for beginners to understand


📌 Technologies Used
1. Python

•Used to build the main program logic

•Connects to PostgreSQL using psycopg2

•Used for GUI (Tkinter / CustomTkinter)


2. PostgreSQL

•Stores all data such as products, customers, and orders

•Provides fast and secure queries

•Uses tables and relationships to manage data


3. SQL

•Used to create tables

•Insert, update, delete data

•Fetch reports


📌 Tools / Libraries

•psycopg2 – for PostgreSQL connection

•Pillow (PIL) – optional, for images

•CustomTkinter – optional GUI

•Tkinter – for UI

•Python 3.10+


📌 How to Run the Project
1. Install Required Python Packages
pip install -r requirements.txt


2. Create PostgreSQL Database

i) Open pgAdmin or terminal

ii) Create a database (example: online_store_db)

iii) Run the SQL file:

iv) psql -U postgres -d online_store_db -f sql/create_tables.sql


3. Update Database Credentials in database.py

(Replace with your actual username, password, db name.)


4. Run the Application
python app.py


📌 Database Tables

•products → product details

•customers → customer info

•orders → order records

•order_items (optional) → items in each order


📌 Screenshot
![Dashboard Screenshot](./Output/Login.png)
![Dashboard Screenshot](./Output/Order%20table.png)
![Dashboard Screenshot](./Output/Product%20Table.png)
