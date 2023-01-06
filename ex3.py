# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input("Input your number: "))
new_list = []

for i in range(1, n+1):
    new_list.append(round(((1+1/i)**i), 3))
print(new_list)

sum = 0
list_len = len(new_list)

for i in range(list_len):
    sum = sum + new_list[i]
print(sum)
