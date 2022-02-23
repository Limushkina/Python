# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 
x = int(input('Введите координату по оси X:'))
y = int(input('Введите координату по оси Y:'))
def coordinate(x, y):
    if x > 0 and y > 0:
        return('Первая четверть')
    if x < 0 and y > 0:
        return('Вторая четверть')
    if x > 0 and y < 0:
        return('Третья четверть')
    if x < 0 and y > 0:
        return('Третья четверть')
    if x < 0 and y < 0:
        return('Четвертая четверть')
    if x == 0 and y == 0:
        return('Начало координат')
print(coordinate(x, y))