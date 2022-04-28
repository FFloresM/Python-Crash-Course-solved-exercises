glossary = {
    'for': 'loop through a container',
    'if': 'make a decision',
    'string': 'chars set',
    'integer': "a whole number",
    'python': 'programming language'
}

for term, meaning in glossary.items():
    print(f'{term}: {meaning}\n')

glossary['list'] = "set of values"
glossary['else'] = "runs if condition is False"
glossary['while'] = "loop as long as the condition is true"
glossary['dict'] = "set of key-value pairs"
glossary['set'] = "a set of data"

for term, meaning in glossary.items():
    print(f'{term}: {meaning}\n')