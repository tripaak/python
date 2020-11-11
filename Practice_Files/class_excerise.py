class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def dicount(self, percentage):
        #self.percentage = percentage
        print(percentage)
        return f"Old Price {self.price}, New Price: {self.price*(percentage/100)}"    




L1 = Laptop('Sony', 'Lumiya', 52000)
L2 = Laptop('Apple', 'MacBook', 1000000)

print(L2.price)

print(L2.dicount(40))
