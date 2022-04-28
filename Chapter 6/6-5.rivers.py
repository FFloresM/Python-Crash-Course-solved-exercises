rivers = {
    'nile': 'egypt',
    'bio-bio': 'chile',
    'amazon': 'brazil'
}

for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country.capitalize()}")

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)