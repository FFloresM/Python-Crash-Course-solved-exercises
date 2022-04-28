favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }
friends = ['phil', 'sarah']

for name in favorite_languages:
    if name in friends:
        print(f"{name} thank you for responding")
    else:
        print(f"{name} plase take the poll")
