class Pizzas:
    def __init__(self) -> None:
        self.idcount = 1
        self.pizzas = []
    
    def __str__(self):
        ret = ""
        for pizza in self.pizzas:
            ret += f"{pizza}\n"
        return ret[:-1]
        
    def createpizza(self, toppings):
        if 1 <= len(toppings) <= 3:
            pizza = Pizza(self.idcount, toppings)
            self.idcount += 1
            self.pizzas.append(pizza)
    
    def servePizza(self, ID):
        for index, pizza in enumerate(self.pizzas):
            if pizza.id == ID:
                self.pizzas[index].served = True
    
    def removeServed(self):
        pizzas = []
        for pizza in self.pizzas:
            if not pizza.served:
                pizzas.append(pizza)
        self.pizzas = pizzas

class Pizza:
    def __init__(self, ID, toppings) -> None:
        self.id = ID
        self.toppings = toppings
        self.served = False
    
    def __str__(self):
        ret = f"ID: {self.id}, Toppings: "
        ret += ", ".join(self.toppings)
        ret += f" Served: {self.served}"
        return ret
