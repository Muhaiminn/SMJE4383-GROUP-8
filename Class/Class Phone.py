class Phone:
    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.name}, {self.brand}, {self.year}"


class SmartPhone(Phone):
    def __init__(self, name, brand, year, operating_system):
        super().__init__(name, brand, year)
        self.operating_system = operating_system

    def smart(self):
        return f"{self.name}, {self.brand}, {self.year}, {self.operating_system}"


class BasicPhone(Phone):
    def __init__(self, name, brand, year, is_touch_screen):
        super().__init__(name, brand, year)
        self.is_touch_screen = is_touch_screen

    def basic(self):
        return f"{self.name}, {self.brand}, {self.year}, {self.is_touch_screen}"

# Creating instance
smartphone = SmartPhone("iPhone 13", "Apple", "2021", "iOS")
basicphone = BasicPhone("Sony Ericsson C902", "Sony", "2008", "No touch screen")

# Accessing method
print (smartphone.info())
print (smartphone.smart())
print (basicphone.info())
print (basicphone.basic())



