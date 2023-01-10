#  4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

import random as r


def float_list(n):
    list_1 = []
    num = 0
    while len(list_1) < n:
        num = round(r.uniform(0.1, n * 5), 2)
        list_1.append(num)
    return list_1


def dif_float(list2):
    new_list = []
    for i in list2:
        i = round(i - int(i), 3)
        new_list.append(i)
    print(new_list)
    return max(new_list) - min(new_list)


a = float_list(int(input('Input number: ')))
print(a)
print(dif_float(a))
