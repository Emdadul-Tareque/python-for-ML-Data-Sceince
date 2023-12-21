class Clothing:
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

    def calculate_discount(self, discount):
        return self.price * (1-discount)
    
    def display_pant(self):
        print(f"color: {self.color}, size: {self.size}, style: {self.style}, price: {self.price}")
    

class Shirt(Clothing):
    def __init__(self, color, size, style, price, long_or_short):
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short

class Pant(Clothing):
    def __init__(self, color, size, style, price, waist):
        Clothing.__init__(self, color, size, style, price)
        self.waist =waist

    def double_price(self):
        self.price = 2 * self.price

    def calculate_discount(self, discount):
        return self.price * (1 - discount/2)
    
    def display_pant(self):
        Clothing.display()

        print(f"color: {self.color}, size: {self.size}, style: {self.style}, price: {self.price}, waist: {self.waist}")
    

new_pant = Pant('blue', 'L', 'long', 1000, 38)

new_pant.display_pant()

