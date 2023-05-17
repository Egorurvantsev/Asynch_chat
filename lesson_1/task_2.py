list_str = [
    'class',
    'function',
    'method'
]

for i in list_str:
    j = bytes(i, 'utf-8')
    print(type(j), j, len(j))