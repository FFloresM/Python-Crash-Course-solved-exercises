valid_age = 0
active = 0
while not valid_age:
    active += 1
    age = input("enter your age: ")
    if age == 'quit':
        break
    else:
        age = int(age)
        if age >=0 and age < 3:
            print("The ticket is free")
            valid_age=1
        elif age >= 3 and age < 12:
            print("The ticket is $10")
            valid_age=1
        elif age >= 12:
            print("The ticket is $15")
            valid_age=1
        else:
            print("Invalid age")
