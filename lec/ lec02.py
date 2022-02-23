# a - открытие для добавления данных r - открытие для чтения данных w - открытие для записи данных

# colours = ['red', 'green', 'blue']
# data = open('file.txt', 'a') 
# # data.writelines(colours)
# data.write('\nLine 12\n') # \n - с новой строки
# data.write('Line 13\n')
# data.close()

# with open('file.txt', 'a') as data:
#     data.write('\nLine4')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import lec01 as l

# print(l.f(2.3))

# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('*', 7))


# def new_def(*counts):
#     res: str = ""
#     for item in counts:
#         res += item
#     return res

# print(new_def('l', 'i', 'm', 'a'))
# print(new_def('1', 'a'))

# число фибоначи
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list=[]
# for e in range(1,10):
#     list.append(fib(e))
# print(list)

# картежи
# a = (3, 2, 54, 4)
# print(a[2])

# for item in a:
#     print(item) 

# словари
# dictionary = {}
# dictionary = \
#     {
#         'up': 'u',
#         'left': 'l',
#         'right': 'r',
#         'down': 'd'
#     }
# print(dictionary)
# print(dictionary['right'])

# for k in dictionary.values():
#     print(k)

# множества
# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('grey')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('grey')
# print(colors)

# from typing import FrozenSet


# a = {1, 4, 2, 7, 9}
# b = {7, 3, 6, 1, 2}
# c = a.copy() #копирование множества
# u = a.union(b)  #объединение множеств
# s = FrozenSet(a) #неизменяемое множество

#списки
# list1 = [1, 2, 3, 4, 5] 
# print(list1.pop(2)) #удаление элемента
# print(list1)
# print(list1.insert(2, 6)) #добавление элемента
# print(list1)
# print(list1.append(34)) #добавление в конец
# print(list1)