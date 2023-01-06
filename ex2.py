# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

n = int(input("Input your number: "))
new_list = []
n1 = 1
n2 = 1
sum = 1
for i in range(1, n+1):
    n2 = n1 * i
    sum = sum * n2
    new_list.append(sum)

print(new_list)
