# Uses Python natural language toolkit (NLTK)
# English words txt file from: https://github.com/dwyl/english-words

import nltk

nltk.download('wordnet')
from nltk.corpus import wordnet as wn

# import ssl


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
        noun_vals = []
        verb_vals = []
        adj_vals = []
        adv_vals = []

        for num in range(0, len(file_vals) - 2):
            val_1_synsets = wn.synsets(file_vals[num])
            if val_1_synsets:
                # finds pos if not empty
                val_1 = val_1_synsets[0].pos()
            else:
                # empty if no value
                val_1 = ""

            if val_1 == "n":
                noun_vals.append(file_vals[num])
            elif val_1 == "v":
                verb_vals.append(file_vals[num])
            elif val_1 == "a":
                adj_vals.append(file_vals[num])
            elif val_1 == "r":
                adv_vals.append(file_vals[num])

        print(noun_vals, "\n", verb_vals, "\n", adj_vals, "\n", adv_vals)

        print(len(noun_vals), len(verb_vals), len(adj_vals), len(adv_vals))
        # print(noun_vals[0], verb_vals[0], sep=" ")

        # Noun + verb sentences TODO: add algo to check grammar validitiy
        for i in range(len(verb_vals)):
            print(noun_vals[i].capitalize(), verb_vals[i].lower(), sep=" ")

        # Noun + verb + adjective sentences
        for i in range(len(adj_vals)):
            print(noun_vals[i].capitalize(), verb_vals[i].lower(), adj_vals[i].lower(), sep=" ")


my_obj = Sentence()
my_obj.joiner(my_obj.open_file())
