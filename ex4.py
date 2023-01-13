#  4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
#  записать в файл полученный многочлен не менее 3-х раз.
import random


def list_1(n=10):
    lst = []
    for i in range(n):
        lst.append(random.choice(range(n)))
    return lst

def polynom(n1, n2, n3, lst, name):
    numbers = [n1, n2, n3]
    with open(f'{name}.txt', 'w') as my_f:
        for n in numbers:
            si = ['+', '-']
            r = 0
            pol = ''
            a = ''
            for i in reversed(range(1, n + 1)):
                a = f'{lst[r]}x^{i} {random.choice(si)}'
                if i == 1:
                    a = f'{lst[r]} = 0 \n'
                elif lst[r] == 0:
                    a = ''
                pol = pol + a
                r += 1
            my_f.write(pol)

polynom(5,8,9,list_1(),'file1')



