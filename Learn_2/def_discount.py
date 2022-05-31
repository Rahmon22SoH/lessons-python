
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

new_price = discounted(100000, 10, name_phone='Iphone 12')
print(new_price)
new_price = discounted(40000, 20, name_phone='samsung s3')
print(new_price)
new_price = discounted(5000, 20)
print(new_price)
    