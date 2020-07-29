pizzas = ["Pepperoni", "Hawaiian", "Vegetarian"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really like pizza!")

friend_pizzas = pizzas[:]

pizzas.append("Meat Lover's")
friend_pizzas.append("Chicken Lover's")

print(f"\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print(f"\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)