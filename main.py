# Uses Python natural language toolkit (NLTK)
# English words txt file from: https://github.com/dwyl/english-words

from PyDictionary import PyDictionary

# 2 Lines commented below are necessary for the first run of program
# import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn

word_list = ['amazing', 'interesting', 'love', 'great', 'nice']  # replace w/ txt file -> needs conversion
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

''' Sentence Patterns:
Subject - Verb - Object
Subject - Verb
Subject - Verb - Adjective
Subject - Verb - Adverb '''


class Sentence:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def open_file(self):
        open_words = open("words.txt", "r")

        print(open_words)

    def joiner(self):
        print(self.value1.capitalize() + " " + self.value2 + ".")


my_obj = Sentence(word_list[1], word_list[2])
my_obj.joiner()

# TODO: CREATE SENTENCES VIA LOOP, FILTERS OUT INVALID SENTENCES, STOPS AT 1000 WORDS
# EXPLAIN IN README EXPANSION POTENTIAL
# PROOF OF CONCEPT

open_words = open("words.txt", "r")

print(open_words)


