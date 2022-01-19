"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
"""
import random

k = random.randint(0, 100)


def choose(q):
    n = input('Введите число: ')
    try:
        n = int(n)
    except:
        print('Вы вместо числа ввели строку')
        return choose(q)
    if n == k:
        return print('Ты угадал')
    elif q == 10:
        return print(f'Кончились 10 попыток. Число было {k}')
    elif n > k:
        print('Неугадали. Число больше загаданного')
    else:
        print('Неугадали. Число меньше загаданного')
    return choose(q + 1)


choose(0)
