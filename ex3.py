# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def reverse(list1):
    len_l = len(list1)
    n_list = []
    for i in range(len_l):
        m = list1[len_l - 1 - i]
        n_list.append(m)
    return n_list


def double_f(n):
    new_list = []
    a = abs(n)
    while a > 1:
        b = a % 2
        a = a // 2
        new_list.append(b)
    else:
        new_list.append(a)
    arr = reverse(new_list)
    res = 0
    for i in arr:
        res = res * 10 + i
    return res


print(double_f(int(input('Input your number: '))))
