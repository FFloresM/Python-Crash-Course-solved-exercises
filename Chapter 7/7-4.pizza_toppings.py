while 1:
    topping = input("enter a topping\n('quit' for finish): ")
    if topping == 'quit':
        break
    elif topping != 'quit':
        print(f"you add {topping} to your pizza")