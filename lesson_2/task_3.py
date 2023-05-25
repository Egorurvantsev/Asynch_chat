import yaml

dict = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_ptice': {'computer': '200\u20ac-1000\u20ac',
                           'printer': '100\u20ac-300\u20ac',
                           'keyboard': '5\u20ac-50\u20ac',
                           'mouse': '4\u20ac-7\u20ac'}
           }


with open('task_3.yaml', 'w') as f_n:
    yaml.dump(dict, f_n, default_flow_style=False, allow_unicode=True)

with open('task_3.yaml') as f_n:
    print(f_n.read())
