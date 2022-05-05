favorite_places= {
    'mike': ['beach'],
    'john': ['river', 'mountain'],
    'will': ['park', 'museum', 'library']
}

for name, places in favorite_places.items():
    print(f'name: {name}\nfavorite places: {" ".join(places)}')