#!/usr/bin/env python3

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
# Move connection inside functions or use a connection context so changes persist properly.

DB_NAME = "Final.sqlite"

def get_connection():
    return sqlite3.connect(DB_NAME)

# Set up the database: create the customers table if it doesn't exist
def setup():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        conn.commit()

# Add a new customer to the database
def add(name, email):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        conn.commit()

# Retrieve all customers from the database
def get_all():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM customers")
        return cursor.fetchall()

# Delete a customer by ID
def delete(customer_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
        conn.commit()
        return cursor.rowcount > 0

# Delete all customers from the database
def delete_all():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers")
        conn.commit()

# Reset the auto-incrementing ID sequence (for SQLite)
def reset_sequence():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'customers'")
        conn.commit()

# Search for customers by name or email
def search(keyword):
    keyword = f"%{keyword}%"
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM customers WHERE name LIKE ? OR email LIKE ?", (keyword, keyword))
        return cursor.fetchall()

# Update a customer's email by ID
def update_email(customer_id, new_email):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE customers SET email = ? WHERE id = ?", (new_email, customer_id))
        conn.commit()
        return cursor.rowcount > 0
