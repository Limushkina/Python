# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

week   = ['Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday',  
              'Friday', 
              'Saturday',
              'Sunday']
a = int(input('Введите день недели:'))
print(week[a-1])
if a == 6 or a==7:
    print('Dayoff')
else:
    print('Workday')