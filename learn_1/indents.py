import random

x = random.randint(0, 10)
print(x)
def more_func(num):
    if x >= 5:
        print('бльше')
    else:
        print('меньше')
print(more_func(x))

x = 0

while x < 10:
    print(x)
    x = x + 1 