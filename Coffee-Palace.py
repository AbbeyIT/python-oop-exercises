class Customers:
    greeting = "Welcome to Coffee Palace"

    def __init__(self, Name, Beverage, Food, Total):
        self.Name = Name
        self.Beverage = Beverage
        self.Food = Food
        self.Total = Total

c_1 = Customers("Nate", "Expresso", "Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappucino", "Tuna Wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latter", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)

print(Customers.greeting)
print(c_2.Name)
print(c_2.Beverage)
print(c_2.Food)
print(c_2.Total)
print(c_4.Name)
print(c_4.Beverage)
print(c_4.Food)
print(c_4.Total)