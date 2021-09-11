# Uses Python natural language toolkit (NLTK)
# English words txt file from: https://github.com/dwyl/english-words

# 2 Lines commented below are necessary for the initial run of program
# import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn
import ssl

word_list = ['a', 'person', 'amazing', 'interesting', 'love', 'great',
             'nice']  # replace w/ txt file -> needs conversion
pos_all = dict()

for word in word_list:
    pos_l = set()
    for tmp in wn.synsets(word):
        if tmp.name().split('.')[0] == word:
            # Part of Speech (pos) Synset: n = noun, v = verb, a = adjective, r = adverb
            pos_l.add(tmp.pos())
    pos_all[word] = pos_l
    # print(word, pos_l)

# print(pos_all)

# contains_s = {'s'} in pos_all.values()
# print(contains_s)

# key_1 = list(pos_all.keys()).index('interesting')
# print(key_1)

''' Sentence Patterns:
Subject - Verb - Object
Subject - Verb
Subject - Verb - Adjective
Subject - Verb - Adverb '''

"""
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context"""



class Sentence:

    def open_file(self):
        file_vals = []
        i = 0
        with open("words.txt", "r") as my_file:
            for line in my_file:
                stripped_line = line.strip()
                file_vals.append(stripped_line)
                i += 1
            return file_vals

    def joiner(self, file_vals):

        for num in range(0, len(file_vals) - 2):
            val_1_synsets = wn.synsets(file_vals[num])
            if val_1_synsets:
                # finds pos if not empty
                val_1 = val_1_synsets[0].pos()
            else:
                # empty if no value
                val_1 = ""

            val_2_synsets = wn.synsets(file_vals[num+1])
            if val_2_synsets:
                val_2 = val_2_synsets[0].pos()
            else:
                val_2 = ""

            val_3_synsets = wn.synsets(file_vals[num+2])
            if val_3_synsets:
                val_3 = val_3_synsets[0].pos()
            else:
                val_3 = ""

            if val_1 == "n" and val_2 == "v" and val_3 == "a":
                print(val_1.capitalize() + " " + file_vals[num] + ", " + val_2 + " " + file_vals[num+1] + val_3 + " " + file_vals[num+2])
            elif val_1 == "n" and val_2 == "v" and val_3 == "r":
                print(val_1.capitalize() + " " + file_vals[num] + ", " + val_2 + " " + file_vals[num + 1] + val_3 + " " + file_vals[num + 2])
            elif val_1 == "n" and val_2 == "v":
                print(val_1.capitalize() + " " + file_vals[num] + ", " + val_2 + " " + file_vals[num+1])
            else:
                pass



my_obj = Sentence()
my_obj.joiner(my_obj.open_file())
