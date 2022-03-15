# Подсчитать сумму цифр в вещественном числе
import math

a = str(input('Введите число:'))
a = a.replace('.', '')
print(sum(map(int,str(a))))
