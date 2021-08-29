# Python natural language toolkit (NLTK)

from PyDictionary import PyDictionary

# 2 Lines commented below are necessary for the first run of program
# import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn


word_list = ['amazing', 'interesting', 'love', 'great', 'nice']
pos_all = dict()

for word in word_list:
    pos_l = set()
    for tmp in wn.synsets(word):
        if tmp.name().split('.')[0] == word:
            # Part of Speech (pos) Synset: n = noun, v = verb, a = adjective, r = adverb
            pos_l.add(tmp.pos())
    pos_all[word] = pos_l
    print(word, pos_l)

# pos_all dictionary - 'key' : set of {'values'}
print(pos_all)

contains_s = {'s'} in pos_all.values()

print(contains_s)

# Finds position of key
key_1 = list(pos_all.keys()).index('interesting')

print(key_1)

