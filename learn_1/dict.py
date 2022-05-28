# Словари / Dictionaries
# Содежат набор элементов в формате ключ : значение
# Выбрать элемент можно по названию ключа
from pprint import pprint # печатьв удобном формате

product = {
    'name': 'samsung',
    'stock': 24,
    'price': 1024.1
}
print(product)
print(len(product))
product['skladsamara'] = 50 # добавление элемента в список через =
print(product)
print(product.get('name')) # поск элемента по ключу с исключением None если эго нет 
del product['stock']
print(product)
phones = ['iPhone SE (3-го поколения) Год выпуска', 'iPhone 13 Pro Max. Год выпуска: 2021', 'iPhone 13 Pro. Год выпуска: 2021'] 
product['reccomend'] = phones
pprint(product['reccomend']) 
pprint(product['reccomend'][0])
product['reccomend'].append('lenovo')
pprint(product )

stok = [
    {'name': 'samsung','stock': 24,'price': 1024.1, 
    'recomend': ['iPhone SE (3-го поколения) Год выпуска', 'iPhone 13 Pro Max. Год выпуска: 2021', 'iPhone 13 Pro. Год выпуска: 2021']},
    {'name': 'lenovo','stock': 24,'price': 10224.1,},
    {'name': 'hp','stock': 24,'price': 1124.1,}
]
pprint(stok[0])








