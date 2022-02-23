# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти?

a = int(input('Введите номер четверти:'))
def num_coordinate(a):
    if a == 1:
        return 'x > 0, y > 0'
    if a == 2:
        return 'x < 0, y > 0'
    if a == 3:
        return 'x < 0, y < 0'
    if a == 4:
        return 'x > 0, y < 0'
    if a > 4:
        return 'Четверть введена неверно'
print(num_coordinate(a))