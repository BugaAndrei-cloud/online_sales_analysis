from product import Product
from product_manager import ProductManager

manager = ProductManager()

# Adăugăm produse
manager.add_product(Product("Laptop", 1500, 10))
manager.add_product(Product("Mouse", 25, 100))
manager.add_product(Product("Keyboard", 45, 50))

# Afișăm produsele și valoarea totală
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()}")
