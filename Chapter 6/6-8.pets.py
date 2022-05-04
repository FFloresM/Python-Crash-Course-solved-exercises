pet1 = {
    "name": "Toby",
    "kind": "dog",
    "owner": "Ted"
}
pet2 = {
    "name": "Tetera",
    "kind": "cat",
    "owner": "Vicky"
}
pet3 = {
    "name": "Punto",
    "kind": "cat",
    "owner": "Javier"
}
pet4 = {
    "name": "Lucas",
    "kind": "parrot",
    "owner": "Grandma pig"
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()