"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if new_node > self.root:
            print(f"Ne tuda, Chislo menshe {self.root} ")
            self.insert_left(int(input(' Vvedite drugoe chislo: ')))
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, new_node):
        if new_node < self.root:
            print(f"Ne tuda, Chislo bolshe {self.root} ")
            self.insert_right(int(input(' Vvedite drugoe chislo: ')))

        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(25)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(6)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
print(r.get_right_child().get_root_val())
