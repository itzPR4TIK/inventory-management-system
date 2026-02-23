from database import (create_table, add_product, view_product, update_name, update_quantity, update_price, update_all, delete_product)

print("Inventory Management System Started")

create_table()

print("Wellcome to te INVENTORY SYSTEM ")
while True:
    print("1 : ADD PRODUCT")
    print("2 : VIEW PRODUCT")
    print("3 : UPDATE PRODUCT")
    print("4 : DELETE PRODUCT")
    print("5 : EXIT")

    choice = int(input("Enter your choice: "))
    try:
        if choice == 1:
            name = input("Enter the name of the Product: ")
            quantity = int(input("Enter the Quantity of the Product: "))
            price = float(input("Enter the Price of the Product: "))

            add_product(name, quantity, price)

            print("Product added successfullly!!")

        elif choice == 2:
            product = view_product()

            if not product:
                print("Inventor is empty")
            else:
                print("\n--- Inventory List ---")
                print("ID | Name | Quantity | Price")
                print("-" * 35)
                for i in product:
                    print(f"{i[0]} | {i[1]} | {i[2]} | {i[3]}")
        elif choice == 3:
            product_id = int(input("Enter Product ID to update: "))

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Quantity")
            print("3. Price")
            print("4. Everything")

            update_choice = input("Enter choice: ")

            if update_choice == "1":
                new_name = input("Enter new name: ")
                update_name(product_id, new_name)
                print("Name updated successfully!")

            elif update_choice == "2":
                new_quantity = int(input("Enter new quantity: "))
                update_quantity(product_id, new_quantity)
                print("Quantity updated successfully!")

            elif update_choice == "3":
                new_price = float(input("Enter new price: "))
                update_price(product_id, new_price)
                print("Price updated successfully!")

            elif update_choice == "4":
                name = input("Enter new name: ")
                quantity = int(input("Enter new quantity: "))
                price = float(input("Enter new price: "))
                update_all(product_id, name, quantity, price)
                print("Product fully updated!")

            else:
                print("Invalid update choice")
        elif choice == 4:
            product_id = int(input("Enter Product ID to delete: "))

            confirm = input("Are you sure? (yes/no): ").lower()

            if confirm == "yes":
                delete_product(product_id)
                print("Product deleted successfully!")
            else:
                print("Deletion cancelled.")
        elif choice == 5:
            print("Exiting Program...")
            break
        else :
            print("INVALID CHOICE")
    except ValueError:
        print("⚠️ Please enter numbers where required.")   