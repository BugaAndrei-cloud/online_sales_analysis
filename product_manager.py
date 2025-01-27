# Importăm clasa Product din product.py
from product import Product

class ProductManager:
    """
    Clasa ProductManager gestionează lista de produse disponibile.
    """
    def __init__(self):
        # Listă pentru stocarea produselor
        self.products = []

    def add_product(self, product):
        """
        Adaugă un produs în lista de produse.

        :param product: Instanță a clasei Product.
        """
        self.products.append(product)

    def display_products(self):
        """
        Afișează toate produsele din lista de produse.
        """
        if not self.products:
            print("Nu există produse disponibile.")
        else:
            print("Produsele disponibile sunt:")
            for product in self.products:
                product.display_info()

    def remove_product(self, name):
        """
        Elimină un produs din lista de produse după nume.

        :param name: Numele produsului de eliminat.
        """
        initial_count = len(self.products)
        self.products = [product for product in self.products if product.name != name]
        if len(self.products) < initial_count:
            print(f"Produsul '{name}' a fost eliminat cu succes.")
        else:
            print(f"Produsul '{name}' nu a fost găsit.")

    def calculate_total_value(self):
        """
        Calculează valoarea totală a tuturor produselor din inventar.

        :return: Valoarea totală a inventarului.
        """
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value
