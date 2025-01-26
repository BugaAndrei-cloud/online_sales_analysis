from product import Product
from product_manager import ProductManager

manager = ProductManager()
manager.add_product(Product("Smartphone", 800, 15))
manager.add_product(Product("Headphones", 50, 200))
manager.add_product(Product("Charger", 20, 100))

# Afișăm produsele și valoarea totală
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()}")

from cart import Cart

# Instanța managerului de produse
manager = ProductManager()
manager.add_product(Product("Laptop", 1500, 10))
manager.add_product(Product("Mouse", 25, 100))
manager.add_product(Product("Keyboard", 45, 50))

# Instanța coșului
cart = Cart()
cart.add_to_cart(manager.products[0], 2)  # Adaugă 2 Laptopuri
cart.add_to_cart(manager.products[1], 5)  # Adaugă 5 Mouse-uri
cart.add_to_cart(manager.products[2], 1)  # Adaugă 1 Tastatură

# Afișează produsele din coș și valoarea totală
cart.display_cart()
print(f"Total Cart Value: {cart.total_cart_value()}")
