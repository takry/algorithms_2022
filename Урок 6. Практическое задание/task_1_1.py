"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""

"""
Урок 2.
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры."""

# Меняем рекурсию на цикл

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


@profile
def count_if(i):
    s = 1
    for i in range(n):
        if i % 2 == 1:
            s = s + ((s / 2) * -1)
        else:
            s = s + (s / 2)
    return print(f'Количество элементов - {n}, их сумма - {s}')


c_r(0)
count_if(0)
