"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""

n = int(input('n = '))


def get_sum(n):
    if n == 0:
        return n
    if n == 1:
        print(f'{n} = ', end='')
        return n + get_sum(n - 1)
    else:
        print(f'{n} + ', end='')
        return n + get_sum(n - 1)


print(get_sum(n))
print(f'{n}({n}+1)/2 = {n * (n + 1) / 2}')
