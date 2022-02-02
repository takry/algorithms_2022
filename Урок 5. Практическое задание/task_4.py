"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def dict_fill():
    a = {x: x ** 2 + 1 for x in range(5)}
    return a


def orderdict_fill():
    b = OrderedDict({x: x ** 2 + 1 for x in range(5)})
    return b


def dict_ch(a):
    print(a[3])
    a[3] = 2 ** 4
    print(a[3])
    return a


def orderdict_ch(b):
    print(b[3])
    b[3] = 2 ** 4
    print(b[3])
    return b


a = dict_fill()
b = orderdict_fill()
dict_ch(a)
orderdict_ch(b)
print(a)
print(b)
print('Заполняем дикт')
print(timeit('dict_fill', setup='from __main__ import dict_fill', number=10000))
print('Заполняем ордердикт')
print(timeit('orderdict_fill', setup='from __main__ import orderdict_fill', number=10000))
print('Работа с элементом дикт')
print(timeit('dict_ch', setup='from __main__ import dict_ch', number=10000))
print('Работа с элементом ордердикт')
print(timeit('orderdict_ch', setup='from __main__ import orderdict_ch', number=10000))
# По скорости операций практичеки идентичны. В версии 3.6 дикты стали упорядоченные,
# что рушит концепцию ордердикта.
# За исключением специфических методов (move_to_end) дикт справляется с задачами ордердикта