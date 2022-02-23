# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
n = int(input('Введите число N:'))
list = [n]
list[0] = 1
for i in range(1, n):
    list.append(list[i-1]* -3)
print(list)