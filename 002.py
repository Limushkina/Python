# Даны два числа. Показать большее и меньшее число
# import random
# a = random.randint(1, 100)
# print(a)
# b = random.randint(1, 100)
# print(b)
# if a > b:
#     print('Наибольшее число =', a, 'Наименьшее число =', b)
# else:
#     print('Наибольшее число =', b, 'Наименьшее число =', a)

# Найти максимальное из пяти чисел
from random import randint

list = []
for i in range(5):
    list.append(randint(1, 100))
print(list)
print(max(list))