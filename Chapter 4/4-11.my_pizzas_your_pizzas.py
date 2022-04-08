pizzas = ['mozzarella', 'pepperoni', 'neapolitan', 'chicago']
friend_pizzas = pizzas[:]
pizzas.append("spain")
friend_pizzas.append("vegetarian")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)