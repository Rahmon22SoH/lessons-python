# Функция 
# вызов из разных мест программы
# функции помогают структурировать код и разбить его на отдельные действия 
# делают код более читабельным и упрощают поиск ошибок
# должна хорошо отражать свое действие 
# Аргументы (могут быть позиционные и именованные)
# функция  это чёрный ящик в который мы можем что-то положить, на выходе получить результат.
# Аргументы - данные с которыми мы будем работать в нутрии функции
# Названия аргументов как у обычных переменных 
# 


def descounting(price, discount):
    price = abs(price) #
    discount = abs(discount) # возвращает число без знака aeyrebz abs
    if discount >= 35:
        pirce_wich_dis = price
    else:
        pirce_wich_dis = price - (price * discount / 100)
    return pirce_wich_dis
    

product = [
    {'name': 'samsung','stock': 24,'price': 1024.1, 'discount': 20,},
    {'name': 'lenovo','stock': 24,'price': 10224.1,'discount': 20},
    {'name': 'hp','stock': 24,'price': 1124.1,'discount': 20}
]
    
 #product['with_discound'] = descounting(product[0]['price'][2])
product = descounting(product[0]['price'],product[0]['discount']) 
print(product)

product = descounting(product[0,1,2]['price'],product[0,1,2]['discount']) # Как рассчитать все колони ( ПРОБЛЕМА с доступом к внутренним элементам словаря и их взаимодействие с функцией)
print(product)
