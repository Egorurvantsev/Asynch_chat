list_str = [
    'attribute',
    'класс',
    'функция',
    'type',
]

for i in list_str:
    try:
        print(bytes(i, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{i}" невозможно записать в виде байтовой строки')