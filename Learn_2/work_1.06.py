stok = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def calculation_statistics(sum_avg):
  stat_product = 0
  for sum_sale in sum_avg:
    stat_product += sum_sale
  return stat_product

product_sum = 0
for all_sales in stok:
    phone_sum = calculation_statistics(all_sales['items_sold'])
print(f"Суммарное количество продаж для каждого товара {phone_sum}")
print(f"Суммарное количество продаж для каждого товара {phone_sum}")



studends_sorces = [2,5,5,4,2,3] 

avg_score = 0
for score in studends_sorces:
    print('До', avg_score)
    avg_score = avg_score + score
    print('После', avg_score)


print('Средн оценка ', avg_score)