# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


list_1 = [1, 7, 1, 2, 6, 2, 1, 4, 5, 1]    # заданный список
list_2 = []                                # итоговый список
list_1_copy = list_1[:]                    # копия списка
for num1, value1 in enumerate(list_1):
    if value1 == "@":                      # повторяющиеся элементы
        continue
    for num2, value2 in enumerate(list_1[num1+1:], start = num1 + 1):
        if value1 == value2:
            list_1[num2] = "@"
    list_2.append(value1)

print(f"список неповторяющихся элементов \n \
исходной последовательности {list_1_copy} \n выглядит так : {list_2} \n")



list_3 = [1, 7, 1, 2, 6, 2, 1, 4, 5, 1] # заданный список
list_3_copy = list_3[:]                   # копия списка
list_4 = []                             # итоговый список
count = 0                               # кол-во повторений
for num3, value3 in enumerate(list_3):
    count = 0
    if value3 == "@":                   # повторяющиеся элементы
        continue
    for num4, value4 in enumerate(list_3[num3+1:], start = num3 + 1):
        if value3 == value4:
            list_3[num4] = "@"
            count += 1
    if count > 0:
        list_3[num3] = "@"
    else:
        list_4.append(value3)
print(f"список неповторяющихся элементов \n \
исходной последовательности {list_3_copy} \n выглядит так : {list_4}")
