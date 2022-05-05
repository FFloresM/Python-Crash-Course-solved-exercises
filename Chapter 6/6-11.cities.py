cities = {
    'chicago': {
        'country': 'usa',
        'population': 2746388,
        'fact': 'the third-most populous city in the United States'
    },
    'Berlin': {
        'country': 'Germany',
        'population': 3769495,
        'fact': 'is the capital and largest city of Germany by both area and population.'
    },
    'Santiago': {
        'country': 'Chile',
        'population': 6269384,
        'fact': 'is the capital and largest city of Chile as well as one of the largest cities in the Americas'
    },
}

for city in cities:
    print(city)
    for key, info in cities[city].items():
        print(f"\t{key}: {info}")