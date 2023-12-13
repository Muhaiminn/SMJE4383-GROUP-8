class HotDrink:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature
        
    def info(self):
        return f"Hot Drink: {self.name}"

class Coffee(HotDrink):
    def __init__(self, name, coffee_type, temperature):
        super().__init__(name, temperature)
        self.coffee_type = coffee_type

    def describe(self):
        print ("Coffee - type: Expresso, temperature: Hot")

class Tea(HotDrink):
    def __init__(self, name, tea_type, temperature):
        super().__init__(name, temperature)
        self.tea_type = tea_type

    def describe(self):
        print ("Tea - type: Green Tea, temperature: Warm")

class HotChocolate(HotDrink):
    def __init__(self, name, chocolate_type, temperature):
        super().__init__(name, temperature)
        self.chocolate_type = chocolate_type

    def describe(self):
        print ("Hot Chocolate - type: Dark Chocolate, temperature: Very Hot")

# Creating instance

coffee = Coffee("Coffee","Expresso","Hot")
tea = Tea("Tea","Green Tea","Warm")
hotchocolate = HotChocolate("Hot Chocolate","Dark Chocolate","Very Hot")

# Accessing method

coffee.describe()
tea.describe()
hotchocolate.describe()
