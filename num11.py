import numpy as np
data = open('data.txt', encoding='utf8').read()
ind_words = data.split()



def make_pairs(ind_words):
    for i in range(len(ind_words)-1):
        if ind_words[i][0].isupper() and (i == 0 or ind_words[i-1][-1] in ".?!\n"):
            yield ('START', ind_words[i])
            yield (ind_words[i], ind_words[i + 1])
        elif ind_words[i][-1] == ".":
            yield (ind_words[i], 'END')
            ('START', ind_words[i+1])
        else:
            yield (ind_words[i], ind_words[i + 1])
    yield (ind_words[-1], 'END')

pair = make_pairs(ind_words)

word_dict = {}
for word_1, word_2 in pair:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

n_sentence = int(input("Введите количество предложений: "))

for i in range(n_sentence):
    first_word = np.random.choice(ind_words)
    while first_word.islower() or first_word[-1] == '.':
        first_word = np.random.choice(ind_words)
    chain = [first_word]
    while chain[-1][-1] not in ".?!\n":
        if chain[-1] == 'END':
            chain.pop()
            chain.append(np.random.choice(word_dict['START']))
        else:
            chain.append(np.random.choice(word_dict[chain[-1]]))
    print(' '.join(chain), end = ' ')

