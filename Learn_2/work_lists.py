stok = [
    {'name': 'samsung','stock': 24,'price': 1024.1, 'discount': 20,},
    {'name': 'lenovo','stock': 24,'price': 10224.1,'discount': 20},
    {'name': 'hp','stock': 24,'price': 1124.1,'discount': 20}
]

def discounted(price, discount, max_discound = 30, name_phone=''):
    price = abs(price) #
    discount = abs(discount)
    max_discound = abs(max_discound)
     # возвращает число без знака  abs
    if max_discound >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discound:
        return price
    elif 'iphone 12' in name_phone.lower() or not name_phone: # Приводим строку к нижнемку регистру 
        return price
    else:
        return price - (price * discount / 100)

for phone in stok:
    phone['price_finel'] = discounted(phone['price'], phone['discount'], name_phone=phone['name'])
print(discounted(100,10,20))

