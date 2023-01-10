# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import *

def sum_num(n):
    new_list = sample(range(1, n * 5), k=n)
    print(new_list)
    sum_i = 0
    for i in range(n):
        if i % 2 == 0:
            sum_i += new_list[i]
    return sum_i

print(sum_num(int(input('Input number: '))))
