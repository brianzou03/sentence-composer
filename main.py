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


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


class Sentence:

    def open_file(self):
        file_vals = []
        i = 0
        with open("words.txt", "r") as my_file:
            for line in my_file:
                if i < 20:
                    stripped_line = line.strip()
                    file_vals.append(stripped_line)
                    i += 1
                else:
                    print(file_vals)
                    return file_vals

    def joiner(self, file_vals):
        val_1_synsets = wn.synsets(file_vals[0])
        if not val_1_synsets:
            val_1 = val_1_synsets[0].pos()
        else:
            val_1 = ""

        val_2_synsets = wn.synsets(file_vals[1])
        if not val_2_synsets:
            val_2 = val_1_synsets[0].pos()
        else:
            val_2 = ""

        if val_1 == "n" and val_2 == "v":
            print(val_1.capitalize() + " " + val_2 + ".")


my_obj = Sentence()
my_obj.joiner(my_obj.open_file())
'''
TODO: CREATE SENTENCES VIA LOOP, FILTERS OUT INVALID SENTENCES, STOPS AT 1000 WORDS
- EXPLAIN IN README EXPANSION POTENTIAL
- PROOF OF CONCEPT
- A VS AN, DIFFERENT PARTS OF SPEECH, 
SENTENCE STRUCTURE DOESN'T WORK FOR EVERYTHING, ETC -> KNOWN ISSUES
'''
