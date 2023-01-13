# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def nums(n):
    new_list = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            new_list.append(i)
            n = n / i
        i += 1
    if n > 1:
        new_list.append(n)
    return new_list


print(nums(int(input('Input: '))))
