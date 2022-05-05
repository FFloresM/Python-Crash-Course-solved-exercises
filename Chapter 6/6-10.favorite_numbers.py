favorite_numbers = {
    "Victoria": [7, 5],
    "Francisco": [7, 9, 3],
    "Felix": [1, 8, 32],
    "Javier": [2, 7],
    "Marcelo": [3]
}

for key in favorite_numbers:
    print(f"name: {key}. Favorite numbers:", *favorite_numbers[key]) #use starred expression: unpack list (can't use starred expression with f-string)