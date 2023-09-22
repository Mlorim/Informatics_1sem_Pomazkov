# class House():
#     def __init__(self, street, number):
#         self.street = street
#         self.number = nember
#
#     def build(self):
#         print("Улица " + self.street + " Дом " + self.number)

# import numpy as np
data = "В теории вероятностей и смежных областях, марковский процесс , названный в честь русского математика Андрея Маркова , является случайным процессом , который удовлетворяет свойство Маркова (иногда характеризуются как « memorylessness »). Грубо говоря, процесс удовлетворяет свойству Маркова , если можно делать прогнозы на будущее процесса , основанного исключительно на его нынешнем состоянии точно так же , как можно было бы знать всю историю процесса, а значит , независимо от такой истории; т.е., условно на нынешнее состояние системы, ее прошлое и будущее государства независимы ."
ind_words = data.split()
def make_pairs(ind_words):
    for i in range(len(ind_words) - 1):
        yield (ind_words[i], ind_words[i + 1])

pair = make_pairs(ind_words)

word_dict = {}
for word_1, word_2 in pair:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]



