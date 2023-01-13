# 1. Вычислить число c заданной точностью d
from decimal import *

n = Decimal(input('Enter a real number: '))
a = input('Enter the required accuracy: ')


print(n.quantize(Decimal(a)))

