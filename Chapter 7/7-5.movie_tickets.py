while 1:
    age = int(input("enter your age: "))
    if age >=0 and age < 3:
        print("The ticket is free")
    elif age >= 3 and age < 12:
        print("The ticket is $10")
    elif age >= 12:
        print("The ticket is $15")
    else:
        print("Invalid age")
