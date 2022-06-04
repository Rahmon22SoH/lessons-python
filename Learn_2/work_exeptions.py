def cat_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except ZeroDivisionError:
        print('Не надо делить на ноль')
    except TypeError:
        print('Сдесь должно быть число а не стока')
print(cat_cake(0))
# Исключения это классы.
# Базовые Exception BaseException
# Исключения ОС ConnectionError TimeoutError 
# Основные ValueError TypeError IndexError KeyError
 