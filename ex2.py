# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import *


def new_list(n):
    n_list = sample(range(1, n * 2), k=n)
    return n_list


def mult_num(list_1):
    list_len = len(list_1)
    n_list = []
    if list_len % 2 == 0:
        for i in range(list_len//2):
            m = list_1[i] * list_1[list_len - 1 - i]
            n_list.append(m)
        print(n_list)
    else:
        for i in range(list_len//2 + 1):
            if i == list_len//2:
                n_list.append(list_1[i])
            else:
                m = list_1[i] * list_1[list_len - 1 - i]
                n_list.append(m)
        return n_list


a = new_list(int(input('Input number: ')))
print(a)
print(mult_num(a))
