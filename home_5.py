# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.


f1 = "-45*x**3 - 6*x**2 + 4*x -1  = 0"       # можно ввести разные коэффициенты и степени(степень до 9)
f2 = "8*x**4 - 4*x**3 + 3*x**2 + -82 = 0"    # в порядке убывания степени


ratio_poly_dict_1 = {}
ratio_poly_dict_2 = {}
result = {}

for i in range(10):
    ratio_poly_dict_1[str(i)]=0
    ratio_poly_dict_2[str(i)]=0

# создание файлов
def file_polynomial(f1, f2):                                     
    with open("file_polynomial_1.txt", "w") as file_1:
        file_1.write(f1)

    with open("file_polynomial_1.txt", "r") as file_2:
        my_file_2 = file_2.read()

    with open("file_polynomial_2.txt", "w") as file_1:
        file_1.write(f2)

    with open("file_polynomial_2.txt", "r") as file_2:
        my_file_4 = file_2.read()

    return my_file_2, my_file_4

# редактирование файлов
def format_files_12(my_file_1: str, my_file_2: str): 

    my_file_1 = my_file_1.replace(" ", "")
    my_file_1 = my_file_1.replace("=0","")
    my_file_1 = my_file_1.replace("-", " -")
    my_file_1 = my_file_1.replace("+", " +")

    my_file_2 = my_file_2.replace(" ", "")
    my_file_2 = my_file_2.replace("=0","")
    my_file_2 = my_file_2.replace("-", " -")
    my_file_2 = my_file_2.replace("+", " +")

    poly_list_1 = my_file_1.split(" ")
    poly_list_2 = my_file_2.split(" ")
    
    return poly_list_1, poly_list_2


# создание словаря коэффициентов (ключ - степень , значение - коэффициент)
def create_ratio_poly_dict(poly_list_1, poly_list_2):
    
    for j in poly_list_1:
        if "*x**" in j:
            j1 = j.split("*x**")
            ratio_poly_dict_1[j1[1]] = j1[0]
        elif "*x" in j:
            j1 = j.split("*")
            ratio_poly_dict_1["1"] = j1[0]
        else:
            ratio_poly_dict_1["0"] = poly_list_1[-1]

    for j in poly_list_2:
        if "*x**" in j:
            j1 = j.split("*x**")
            ratio_poly_dict_2[j1[1]] = j1[0]
        elif "*x" in j:
            j1 = j.split("*")
            ratio_poly_dict_2["1"] = j1[0]
        else:
            ratio_poly_dict_2["0"] = poly_list_2[-1]
    
# подсчёт суммы коэффициентов
def sum_coefficients():                              
   
    for i in range(10):
        
        result[str(i)] = int(ratio_poly_dict_1[str(i)]) \
                       + int(ratio_poly_dict_2[str(i)])

# создание итоговой стоки               
def new_expression():
    new_str = ''
    new_list = sorted(result.items(), reverse=True)
    for i,j in new_list:
        if j == 0:                        # игнорирование коэффициентов со значением ноль
            continue
        if int(i) > 1:
            new_str += str(j)+f"*x**{i}@"
        elif int(i) == 1:
            new_str += str(j)+f"*x@"
        else:
            new_str += str(j)+"@= 0"
    new_str = new_str.replace("@"," + ")
    new_str = new_str.replace("+ -","- ")
    new_str = new_str.replace("+ =","=")
    print(new_str)
    return new_str

# запись в файл
def sum_of_polynom (str_):
    with open("file_polynomial_result.txt", "w") as file_1:
        file_1.write(str_)



file_polynomiales = file_polynomial(f1, f2)
poly_lists = format_files_12(file_polynomiales[0], file_polynomiales[1])

create_ratio_poly_dict(poly_lists[0], poly_lists[1])

sum_coefficients()
print("даны два уравнения ",f1,f2,"суммируем и получаем следующее ",sep = "\n")

str_ = new_expression()

sum_of_polynom (str_)
