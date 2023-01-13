# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
import random


def list_1(n):
    if n < 0:
        print('Negative value of the number of numbers!')
    lst = []
    for i in range(n):
        lst.append(random.choice(range(n)))
    return lst


def uniq(lst):
    uniq_lst = []
    for i in lst:
        if lst.count(i) == 1:
            uniq_lst.append(i)
    return uniq_lst

a = list_1(int(input('Input: ')))

print(a)
print(uniq(a))
