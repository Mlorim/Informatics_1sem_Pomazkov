class Tree():
    def __init__(self, age, tree_type, country, color='green'):
        self.__color = color
        self.age = age
        self.tree_type = tree_type
        self.country = country

    def get_age(self):
        return 'Возраст дерева равен ' + str(self.age)

    def print_country(self):
        print('Данное дерево произрастает в стране ' + self.country)


class FruitTree(Tree):
    def __init__(self, age, tree_type, country, crop):
        super().__init__(age, tree_type, country)
        self.crop = crop

    def get_harvest(self):
        print('Урожай с данного дерева: ' + str(self.crop * self.age))


class NonFruitTree(Tree):
    def __init__(self, age, tree_type, country, wood):
        super().__init__(age, tree_type, country)
        self.wood = wood

    def can_it_be_used(self):
        if self.wood:
            print('Это дерево можно использовать для заготовки древесины.')
        else:
            print('Это дерево нельзя использовать для заготовки древесины.')


tree1 = FruitTree(50, 'Apple', 'Russia', 40)
tree1.get_harvest()
print(tree1.get_age())

tree2 = NonFruitTree(100, 'Pineapple', 'Finland', False)
tree2.can_it_be_used()