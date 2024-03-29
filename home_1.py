# Вычислить число пи c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#-------------------------------------------------------------------------------------------------

# Расчёт ведём по ряду Нилаканта рекурсивным методом:
# π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...
from decimal import Decimal

d = input("Введите точнсть для чиса пи в формате '0.00001' \
где после запятой кол-во знаков,кот.вы хотите видеть  ")

def signs_of_pi(a):
    if a > 10**3:
        return 3
    my_pi = Decimal(4/(a * (a+1) * (a+2)) - 4/((a + 2) * (a + 3) * (a + 4)))
    return signs_of_pi(a+4) + my_pi


print("Число пи методом Нилаканта будет равно ",signs_of_pi(2).quantize(Decimal(d)))

#-------------------------------------------------------------------------------------------------

# вычисление с помощью ряда Лейбница циклом
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
result = 0
for i in range(1,10000000,4):
    result += Decimal(4/i - 4/(i+2))

print("Число пи методом Лейбница будет равно ",result.quantize(Decimal(d)))

print()