#!/usr/bin/env python3

import db

# Set up the database
def setup_database():
    db.setup()

# Add a new customer with basic validation
def add_customer(name, email):
    if not name or not email:
        raise ValueError("Name and email cannot be empty.")
    db.add(name.strip(), email.strip())

# List all customers
def list_customers():
    return db.get_all()

# Remove customer by ID and return True/False
def remove_customer(customer_id):
    return db.delete(customer_id)

# Reset all customers and the ID sequence
def reset_customer_ids():
    db.delete_all()
    db.reset_sequence()

# Search for customers by name or email
def search_customers(keyword):
    return db.search(keyword.strip())

# Update a customer's email by ID
def update_customer_email(customer_id, new_email):
    if not new_email:
        raise ValueError("Email cannot be empty.")
    return db.update_email(customer_id, new_email.strip())
