"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""

# 1)
print(f'# 1)')
from collections import defaultdict
from functools import reduce

a = input('Введите первое число: ')
b = input('Введите второе число: ')
d = defaultdict()
d[a] = int(a, 16)
d[b] = int(b, 16)


def custom_sum(first, second):
    return f'{first + second:x}'


def custom_add(first, second):
    return f'{(first * second):x}'


print(f' Сумма: {a} + {b} = {reduce(custom_sum, d.values())}')
print(f' Произведение: {a} * {b} = {reduce(custom_add, d.values())}')


# 2)
print(f'# 2)')
class A:
    def __init__(self, a1):
        self.a = a1

    def __add__(self, other):
        return A(f'{(int(self.a, 16) + int(other.a, 16)):x}')

    def __mul__(self, other):
        return A(f'{(int(self.a, 16) * int(other.a, 16)):x}')

    def __str__(self):
        return f'{self.a}'


x = A(a)
y = A(b)
print(f'Сумма: {x} + {y} = {x+y}')
print(f'Произведение: {x} * {y} = {x*y}')

