# Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
num = int(input("Введите число : "))
list_1 = []


def simple_mult(a):
    for i in range(2,a + 1):
        if a == i:
            list_1.append(i)
            return 
        if a % i == 0:
            list_1.append(i)
            return simple_mult(a//i)
    return 
simple_mult(num)
print(f"Список простых множителей числa {num} равен ",list_1)