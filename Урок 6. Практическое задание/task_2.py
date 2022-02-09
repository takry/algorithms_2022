"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""

# Оборачиваем функцию в функцию


n = int(input('Введите количество элементов: '))
s = 1

from memory_profiler import profile


@profile
def c_r(i):
    def count_recur(i):
        global s
        if i == n:
            return print(f'Количество элементов - {n}, их сумма - {s}')
        if i % 2 == 1:
            s = s + ((s / 2) * -1)
        else:
            s = s + (s / 2)
        return count_recur(i + 1)

    return count_recur(i)