class Books:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self._price_= price # private attribute - hide as it should not be accessed directly

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Price must be positive.")
        

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"
    
class EBook(Books):
    def __init__(self, title, author, price, file_format):
        super().__init__(title, author, price)
        self.file_format = file_format

    def __str__(self):
        return f"{super().__str__()}, Format: {self.file_format}"

