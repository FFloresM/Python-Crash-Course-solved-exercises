cities = {
    'chicago': {
        'country': 'usa',
        'population': 2746388,
        'fact': 'the third-most populous city in the United States',
        'places to visit': ['Downtown Chicago', 'Willis Toer', 'Navy Pier']
    },
    'Berlin': {
        'country': 'Germany',
        'population': 3769495,
        'fact': 'is the capital and largest city of Germany by both area and population.',
        'places to visit': ['Brandenburg Gate', 'Berlin Cathedral', 'Charlottenburg Palace']
    },
    'Santiago': {
        'country': 'Chile',
        'population': 6269384,
        'fact': 'is the capital and largest city of Chile as well as one of the largest cities in the Americas',
        'places to visit': ['Statue of the Immaculate Conception', 'Santa Lucia Hill', 'La Moneda Palace']
    },
}

for city, info in cities.items():
    print(city)
    for key, value in info.items():
        if key == 'places to visit':
            print(f"\t{key}:", ", ".join(value))
        else:
            print(f"\t{key}: {value}")
        