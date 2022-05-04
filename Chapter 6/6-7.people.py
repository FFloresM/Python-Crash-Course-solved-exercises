person1 = {
    "first_name": "Victoria",
    "last_name": "Vergara",
    "age": 29,
    "city": "Concepción"
}
person2 = {
    "first_name": "Francisco",
    "last_name": "Flores",
    "age": 29,
    "city": "Concepción"
}
person3 = {
    "first_name": "Félix",
    "last_name": "Flores",
    "age": 1,
    "city": "Concepción"
}

people = [person1, person2, person3]

for person in people:
    for k,v in person.items():
        print(f"{k}: {v}")
    print() # new line