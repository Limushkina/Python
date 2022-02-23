# Найти расстояние между двумя точками пространства
x1 = int(input('Введите координаты первой точки по оси X:'))
y1 = int(input('Введите координаты первой точки по оси Y:'))
x2 = int(input('Введите координаты второй точки по оси X:'))
y2 = int(input('Введите координаты второй точки по оси Y:'))

import math
def distance(x1, x2, y1, y2):
    num = (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)
    dis = math.sqrt(num)
    return dis

print(distance(x1, x2, y1, y2))