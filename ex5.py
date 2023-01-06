# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random

import random

n = int(input('Input number: '))
new_list = []

for i in range(n):
    new_list.append(i)

print(new_list)

new_list2 = []

while len(new_list2) < len(new_list):
    k = random.randint(0, n-1)
    if new_list[k] not in new_list2:
        new_list2.append(new_list[k])
print(new_list2)