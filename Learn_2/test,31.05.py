first_line = 'fhdhdfh learn ghfgh'
second_line = 'fhdhdfh learn'
if type(first_line and second_line) != str:
    print(0)
elif first_line != second_line and " learn " in (" " + second_line + " "):
    print(3)
elif first_line != second_line and len(first_line) > len(second_line):
    print(2)
elif first_line == second_line:
    print(1)





# Проверить, является ли то, что передано функции, строками. 
 # Если нет - вернуть 0 +
# Если строки одинаковые, вернуть 1+
# Если строки разные и первая длиннее, вернуть 2
# Если строки разные и вторая строка 'learn', возвращает 3
# Вызвать функцию несколько раз, передавая ей разные праметры 
# и выводя на экран результаты