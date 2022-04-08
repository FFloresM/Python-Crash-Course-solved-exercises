my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]
my_foods.append('cannoli')
friend_food.append('ice cream')
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_food:
    print(food)