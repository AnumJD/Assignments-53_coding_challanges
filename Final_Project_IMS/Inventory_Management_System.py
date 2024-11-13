inventory = {}

users = {
    "admin": "adminpass",
    "user": "userpass"
}

def authenticate(username: str, password: str) -> bool:
    return users.get(username) == password

def add_item(name: str, price: float, stock: int) -> None:
    inventory[name] = {"price": price, "stock": stock}
    print(f"Item {name} added.")

def update_stock(name: str, stock: int) -> None:
    if name in inventory:
        inventory[name]["stock"] += stock
        print(f"Updated stock for {name}. New stock: {inventory[name]['stock']}")
    else:
        print(f"Item {name} not found.")

def search_item(name: str) -> None:
    if name in inventory:
        print(f"Item: {name}, Price: {inventory[name]['price']}, Stock: {inventory[name]['stock']}")
    else:
        print(f"Item {name} not found.")

def display_inventory() -> None:
    if inventory:
        for name, details in inventory.items():
            print(f"Item: {name}, Price: {details['price']}, Stock: {details['stock']}")
    else:
        print("No items in inventory.")

def main():
    print("Welcome to the Inventory Management System!")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate(username, password):
        print(f"Welcome, {username}!")

        while True:
            print("\n1. Add Item")
            print("2. Update Stock")
            print("3. Search Item")
            print("4. Display Inventory")
            print("5. Exit")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue

            if choice == 1:
                item_name = input("Enter item name: ")
                try:
                    price = float(input("Enter price: "))
                    stock = int(input("Enter stock quantity: "))
                    add_item(item_name, price, stock)
                except ValueError:
                    print("Invalid input. Please enter valid price and stock values.")
            elif choice == 2:
                item_name = input("Enter item name to update: ")
                try:
                    stock = int(input("Enter stock quantity to update: "))
                    update_stock(item_name, stock)
                except ValueError:
                    print("Invalid input. Please enter a valid stock value.")
            elif choice == 3:
                item_name = input("Enter item name to search: ")
                search_item(item_name)
            elif choice == 4:
                display_inventory()
            elif choice == 5:
                print("Exiting system.")
                break
            else:
                print("Invalid option. Try again.")
    else:
        print("Authentication failed. Incorrect username or password.")

if __name__ == "__main__":
    main()
