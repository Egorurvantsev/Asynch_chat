import json

def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        f_n.write(json.dumps(dict_to_json, ensure_ascii=False, indent=4))


write_order_to_json(input('Введите название товара: '),
                    input('Введите кол-во товара: '),
                    input('Введите цену товара: '),
                    input('Введите имя покупателя товара: '),
                    input('Введите дату товара: ')
                    )


