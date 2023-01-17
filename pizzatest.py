from pizzas import Pizzas

pizzas = Pizzas()

pizzas.createpizza(["Pepperoni", "piparostur"])
pizzas.createpizza(["ostur", "skinka"])

print(pizzas)

pizzas.servePizza(2)
print()
print(pizzas)

pizzas.removeServed()
print()
print(pizzas)

pizzas.createpizza(["skinka", "ananas", "heil fokking pera í miðjunni!"])
print()
print(pizzas)
