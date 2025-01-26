from product import Product
from product_manager import ProductManager

manager = ProductManager()
manager.add_product(Product("Smartphone", 800, 15))
manager.add_product(Product("Headphones", 50, 200))
manager.add_product(Product("Charger", 20, 100))

# Afișăm produsele și valoarea totală
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()}")
