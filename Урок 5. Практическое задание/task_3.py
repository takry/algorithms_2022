"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""
from collections import deque
import time

# 1)
st = time.time()
a = [1, 2, 3]
print(f'Время создания лист - {time.time() - st}')
st = time.time()
b = deque(a)
print(f'Время создания дек - {time.time() - st}')
st = time.time()
a.append(4)
print(f'Время аппенд лист - {time.time() - st}')
st = time.time()
b.append(4)
print(f'Время аппенд дек - {time.time() - st}')
st = time.time()
a.extend([5, 6])
print(f'Время экстенд дек - {time.time() - st}')
st = time.time()
b.extend([5, 6])
print(f'Время экстенд дек - {time.time() - st}')

# Лист создается быстрее, по аппенду и экстенду цифры +- равны

print('2)')
# 2)
st = time.time()
b.appendleft(1)
print(f'Время аппендлефт дек - {time.time() - st}')
st = time.time()
a.insert(0, 1)
print(f'Время аппендлефт лист - {time.time() - st}')
st = time.time()
b.popleft()
print(f'Время поплефт дек - {time.time() - st}')
st = time.time()
a.pop(0)
print(f'Время поплефт лист - {time.time() - st}')
st = time.time()
b.extendleft([1, 2])
print(f'Время поплефт дек - {time.time() - st}')
st = time.time()
a.insert(0, [1, 2])
print(f'Время поплефт лист - {time.time() - st}')

# Функции слева быстрее обрабатываются деком

print('3)')
# 3)
st = time.time()
print(b[2])
print(f'Время получения элемента дек - {time.time() - st}')
st = time.time()
print(a[2])
print(f'Время получения элемента лист - {time.time() - st}')

# Во взятии элемента по индексу лист быстрее