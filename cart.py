class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        self.cart_items.append({"product": product, "quantity": quantity})

    def total_cart_value(self):
        return sum(item["product"].price * item["quantity"] for item in self.cart_items)

    def display_cart(self):
        for item in self.cart_items:
            product = item["product"]
            quantity = item["quantity"]
            print(f"Product: {product.name}, Quantity: {quantity}, Subtotal: {product.price * quantity}")
