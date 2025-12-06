#!/usr/bin/env python3
import business

# Print a visual separator line
def display_separator():
    print("=" * 60)

# Display app title banner
def display_title():
    display_separator()
    print("                  Customer Management App")
    display_separator()

# Show menu options to the user
def display_menu():
    print()
    print("MENU OPTIONS")
    print("1 - List all customers")
    print("2 - Add customer")
    print("3 - Remove customer")
    print("4 - Search customer")
    print("5 - Update customer email")
    print("6 - Exit program")
    print()
    display_separator()

# List all customers in formatted table
def list_all_customers():
    customers = business.list_customers()
    if customers:
        print(f"{'ID':<5} {'Name':<20} {'Email'}")
        print("-" * 60)
        for cid, name, email in customers:
            print(f"{cid:<5} {name:<20} {email}")
    else:
        print("No customers found.")
    print()

# Prompt user to add a new customer
def add_customer():
    name = input("Enter customer name: ").strip()
    email = input("Enter customer email: ").strip()
    try:
        business.add_customer(name, email)
        print(f"Customer '{name}' added.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Failed to add customer: {e}")
    print()

# Prompt user to remove customer by ID
def remove_customer():
    try:
        cid = int(input("Enter customer ID to remove: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    if business.remove_customer(cid):
        print(f"Customer ID {cid} removed.")
        if not business.list_customers():
            business.reset_customer_ids()  # Reset ID sequence if no customers remain
    else:
        print("Customer not found.")
    print()

# Prompt user to search customers by name or email keyword
def search_customer():
    keyword = input("Enter name or email to search: ").strip()
    results = business.search_customers(keyword)
    if results:
        print(f"{'ID':<5} {'Name':<20} {'Email'}")
        print("-" * 60)
        for cid, name, email in results:
            print(f"{cid:<5} {name:<20} {email}")
    else:
        print("No matching customers found.")
    print()

# Prompt user to update a customer's email by ID
def update_customer_email():
    try:
        cid = int(input("Enter customer ID to update: ").strip())
    except ValueError:
        print("Invalid ID.")
        return

    new_email = input("Enter new email: ").strip()
    if not new_email:
        print("Email cannot be empty.")
        return

    try:
        if business.update_customer_email(cid, new_email):
            print(f"Customer ID {cid} email updated.")
        else:
            print("Customer not found or email not updated.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Failed to update email: {e}")
    print()

# Main loop of the app
def main():
    business.setup_database()
    display_title()
    display_menu()

    while True:
        choice = input("Enter choice: ").strip()
        if choice == "1":
            list_all_customers()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            remove_customer()
        elif choice == "4":
            search_customer()
        elif choice == "5":
            update_customer_email()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            display_menu()

if __name__ == "__main__":
    main()
