class cars:
    def __init__(self, brand, color, model, year, for_sale):
        self.model = model
        self.brand = brand
        self.color = color
        self.year = year
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive {self.brand} {self.model} {self.year}")
    def stop(self):
        print(f"You stop {self.brand} {self.model} {self.year}")
    def describe(self):
        print(f"This is a {self.brand} {self.model} {self.year} and, is for sale: {self.for_sale}")