balanse = 100
price = 50 
in_stoc = 0

if balanse > price and in_stoc:
    print("Одобряем покупку")
elif not in_stoc:
    print('товара нет в наличии')
elif balanse < price:
    print('Покупка не одобрена, пополните баланс')
