class Phone:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")


class SmartPhone(Phone):
    def __init__(self, brand, model, color, operating_system):
        super().__init__(brand, model, color)
        self.operating_system = operating_system

    def text(self, number, message):
        print(f"Sending text to {number}: {message} from {self.brand} {self.model}")


class BasicPhone(Phone):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)


# Creating a smartphone instance
iphone = SmartPhone("Apple", "iPhone 12", "black", "iOS")
print(iphone.brand)
print(iphone.model)
print(iphone.color)
print(iphone.operating_system)

# Creating a basic phone instance
nokia = BasicPhone("Nokia", "1100", "black")
print(nokia.brand)
print(nokia.model)
print(nokia.color)