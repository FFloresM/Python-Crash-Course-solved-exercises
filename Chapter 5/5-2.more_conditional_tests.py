my_name = "Francisco"
print("Is my_name == 'Francisco'? I predict True.")
print(my_name == 'Francisco')

print("\nIs my_name == 'francisco'? I predict False.")
print(my_name == 'francisco')

print("\nIs my_name.lower() == 'francisco'? I predict True.")
print(my_name.lower() == 'francisco')

print("\nIs my_name.lower() == 'Francisco'? I predict False.")
print(my_name.lower() == 'Francisco')

number = 100
print("Is number > 10? I predict True.")
print(number > 10)

print("Is number negative? I predict False.")
print(number < 0)

print("Is number positive or zero? I predict True.")
print(number >= 0)

print("Is number negative or zero? I predict False.")
print(number <= 0)

print("Is number other than 99? I predict True.")
print(number != 99)

print("Is number between 0 and 1000? I predict True.")
print(number > 0 and number < 1000)

print("Is number equal to 0 or 100? I predict True.")
print(number == 0 or number < 1000)

my_list = [1,2,3,4,5]
print("Is 5 in my_list? I predict True")
print(5 in my_list)

print("Is 10 not in my_list? I predict True")
print(10 not in my_list)
