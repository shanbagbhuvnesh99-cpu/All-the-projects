# Coffee Ordering App (Basic)

def display_menu():
    print("\n===== Coffee Menu =====")
    print("1. Cappuccino (S) - 100rs")
    print("2. Cappuccino (M) - 150rs")
    print("3. Cappuccino (L) - 200rs")
    print("4. Americano (S) - 150rs")
    print("5. Americano (M) - 200rs")
    print("6. Americano (L) - 250rs")
    print("7. Cold Coffee - 150rs")
    print("8. Checkout & Exit")


menu_items = {
    1: ("Cappuccino", "Small", 100),
    2: ("Cappuccino", "Medium", 150),
    3: ("Cappuccino", "Large", 200),
    4: ("Americano", "Small", 150),
    5: ("Americano", "Medium", 200),
    6: ("Americano", "Large", 250),
    7: ("Cold Coffee", "Regular", 150)
}


# --- CART FUNCTIONS ---

def add_to_cart(cart, item):
    # item = {name, size, sugar, milk, price, quantity}
    for existing in cart:
        if (existing["name"] == item["name"] and
            existing["size"] == item["size"] and
            existing["sugar"] == item["sugar"] and
            existing["milk"] == item["milk"]):
            
            existing["quantity"] += 1
            return
    
    cart.append(item)


def get_total(cart):
    return sum(i["price"] * i["quantity"] for i in cart)


# --- MAIN APP ---

cart = []

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 8:
        print("\n===== Your Cart =====")
        for item in cart:
            print(f"{item['name']} ({item['size']}), Sugar: {item['sugar']}, Milk: {item['milk']} x{item['quantity']} = {item['price'] * item['quantity']}rs")
        print(f"\nTotal: {get_total(cart)} rs")
        print("Thanks for ordering!")
        break

    if choice not in menu_items:
        print("Invalid choice! Try again.")
        continue

    name, size, price = menu_items[choice]

    sugar = input("Sugar (0-3): ")
    milk = input("Milk (Whole/Toned/Skimmed/No Milk): ")

    item = {
        "name": name,
        "size": size,
        "sugar": sugar,
        "milk": milk,
        "price": price,
        "quantity": 1
    }

    add_to_cart(cart, item)
    print(f"\nAdded to cart: {name} ({size}) with {sugar} sugar + {milk} milk for {price}rs")
