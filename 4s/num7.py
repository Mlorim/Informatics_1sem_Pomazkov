import string
import math

text = []
freq = {}

while True:
    sent = input().lower()
    if sent == '<endofdocument>':
        break

    sent_mod = sent

    for let in sent_mod:
        if let in string.punctuation:
            sent_mod = sent_mod.replace(let, '')

    sent_mod = sent_mod.split()

    for word in set(sent_mod):
        if word not in freq.keys():
            freq[word] = 1
        else:
            freq[word] += 1

    text.append(sent_mod)

tfidf_all = []

freq_srt = [i for i in freq.keys() if i != 'a']
freq_srt.sort()

for sent in text:
    tfidf = []
    for word in freq_srt:
        tf = sent.count(word) / len(sent)
        idf = math.log((len(text) / freq[word])) + 1
        tfidf.append(round(tf * idf, 3))
    tfidf_all.append(tfidf)

for i in range(len(tfidf_all[0])-1):
    print(tfidf_all[0][i], end=', ')

print(tfidf_all[0][-1])
