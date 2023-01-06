# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

n = int(input('Input your number: '))
p1 = int(input('Input position 1: '))
p2 = int(input('Input position 2: '))
new_list = []

for i in range(n * (-1), n+1):
    new_list.append(i)


print(new_list)
print(new_list[p1-1]*new_list[p2-1])