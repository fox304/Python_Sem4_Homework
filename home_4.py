# Задана натуральная степень k.
# Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



from random import randint

k = int(input("Введите натуральную степень :"))
my_list = []
my_str = ""

for i in range(k+1):
    my_list.append(randint(-10, 10))          # здесь можно выбрать любой разбег коэффициентов

for i in range(k+1):
    if my_list[i] == 0:                       # игнорирование нулевых коэффициентов
        continue
    if k-i == 1:
        my_str += f'{my_list[i]}*x '          # редактирование икса со степенью один
    elif k-i == 0:
        my_str += f'{my_list[i]} '            # редактирование икса со степенью ноль
    else:
        my_str += f'{my_list[i]}*x**{k-i} '


my_str = my_str.replace(' ', ' + ')        # шлифуем 
my_str = my_str.replace('+ -', '- ')       # шлифуем
my_str = my_str.rstrip("+ ") + " = 0"      # шлифуем

with open("file_1.txt", "w") as my_file:
    my_1 = my_file.write(my_str)