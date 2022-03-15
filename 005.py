# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
# import random
# a = random.randint(1, 1000)
# print(a)
a = int(input('Введите число:'))

if a % 10 == 0 and a % 15 == 0 and a % 30 != 0:
    print(True)
else:
    print(False)