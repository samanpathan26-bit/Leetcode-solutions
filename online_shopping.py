class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price

    def display(self):
        print("product_id:",self.product_id)
        print("name:",self.name)
        print("price:",self.price)

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]["quantity"] += quantity
        else:
            self.items[product.product_id] = {
                "product": product,
                "quantity": quantity
            }

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            print("Item removed.")
        else:
            print("Product not found.")

    def display_cart(self):
        total = 0

        print("\nCart Items")
        print("-" * 40)

        for item in self.items.values():
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity
            total += subtotal

            print(product.name)
            print("Quantity:", quantity)
            print("Subtotal:", subtotal)
            print()

        print("Total =", total)

    def calculate_total(self):
        total = 0

        for item in self.items.values():
            total += item["product"].price * item["quantity"]

        return total
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = Cart()

    def display(self):
        print("Customer ID:", self.customer_id)
        print("Customer Name:", self.name)
class Order:
    def __init__(self, customer):
        self.customer = customer

    def checkout(self):
        total = self.customer.cart.calculate_total()

        discount = 0

        if total >= 5000:
            discount = total * 0.10
        elif total >= 2000:
            discount = total * 0.05

        final_amount = total - discount

        print("\n------ BILL ------")
        print("Customer:", self.customer.name)
        print("Total:", total)
        print("Discount:", discount)
        print("Amount to Pay:", final_amount)
# Create products
p1 = Product(101, "Laptop", 50000)
p2 = Product(102, "Mouse", 800)
p3 = Product(103, "Keyboard", 1500)

# Store products in a dictionary
products = {
    101: p1,
    102: p2,
    103: p3
}

# Create customer
name = input("Enter customer name: ")
customer = Customer(1, name)

while True:
    print("\n===== ONLINE SHOPPING CART =====")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nAvailable Products")
        for product in products.values():
            product.display()
            print()

    elif choice == 2:
        pid = int(input("Enter Product ID: "))
        qty = int(input("Enter Quantity: "))

        if pid in products:
            customer.cart.add_item(products[pid], qty)
            print("Product added successfully.")
        else:
            print("Invalid Product ID.")

    elif choice == 3:
        pid = int(input("Enter Product ID to remove: "))
        customer.cart.remove_item(pid)

    elif choice == 4:
        customer.cart.display_cart()

    elif choice == 5:
        order = Order(customer)
        order.checkout()

    elif choice == 6:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")