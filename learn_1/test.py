from pprint import pprint 

stok = [
    {'name': 'samsung','stock': 24,'price': 1024.1, 
    'recomend': ['iPhone SE (3-го поколения) Год выпуска', 'iPhone 13 Pro Max. Год выпуска: 2021', 'iPhone 13 Pro. Год выпуска: 2021']},
    {'name': 'lenovo','stock': 24,'price': 10224.1,},
    {'name': 'hp','stock': 24,'price': 1124.1,}
]
pprint(stok[0]['recomend'][0])
stok[0]['recomend'].append('asus')
print(stok[0]['recomend'])
stok[0]['price'] = stok[0]['price'] - 500
print(stok[0]['price'])
stok[1]['name'] = stok[1] = 'asus'
print(stok[1])
print(stok[2]['price'])


