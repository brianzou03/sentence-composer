# Uses Python natural language toolkit (NLTK)
# English words txt file from: https://github.com/dwyl/english-words
# Grammar parsing uses GingerIt, which takes a while to parse each sentence individually

import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from gingerit.gingerit import GingerIt


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

    def composer(self, file_vals):
        noun_vals, verb_vals, adj_vals, adv_vals, other_vals = ([] for i in range(5))

        for num in range(0, len(file_vals) - 2):
            value_synsets = wn.synsets(file_vals[num])
            if value_synsets:
                # finds pos if not empty
                value = value_synsets[0].pos()
            else:
                # empty if no value
                value = ""

            if value == "n":
                noun_vals.append(file_vals[num])
            elif value == "v":
                verb_vals.append(file_vals[num])
            elif value == "a":
                adj_vals.append(file_vals[num])
            elif value == "r":
                adv_vals.append(file_vals[num])
            else:
                other_vals.append(file_vals[num])

        # print(noun_vals, "\n", verb_vals, "\n", adj_vals, "\n", adv_vals)

        # print(len(noun_vals), len(verb_vals), len(adj_vals), len(adv_vals))

        # Noun + verb sentences
        for i in range(len(verb_vals)):
            parser = GingerIt()
            parsed_item = noun_vals[i].capitalize() + " " + verb_vals[i].lower()
            print(parser.parse(parsed_item))

        # Noun + verb + adjective sentences
        for i in range(len(adj_vals)):
            parser = GingerIt()
            parsed_item = noun_vals[i].capitalize() + " " + verb_vals[i].lower() + " " + adj_vals[i].lower()
            print(parser.parse(parsed_item))

        # Noun + verb + adverb sentences
        for i in range(len(adv_vals)):
            parser = GingerIt()
            parsed_item = noun_vals[i].capitalize() + " " + verb_vals[i].lower() + " " + adv_vals[i].lower()
            print(parser.parse(parsed_item))


my_obj = Sentence()
my_obj.composer(my_obj.open_file())
