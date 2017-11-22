import json
import os, sys

def load_words():
    try:
        filename = os.path.dirname(sys.argv[0])+"words_dictionary.json"
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

def load_4_letter_words(my_dict):
    four_letter_word = []
    fh = open('four_letter_words.txt', 'w')
    for idx, val in enumerate(my_dict):

        if len(val) == 4:
            four_letter_word.append(val)
            fh.write(str(val)+ '\n')
    fh.close()        
    return four_letter_word


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print repr(len(load_4_letter_words(english_words)))
    #print(english_words["fate"])
    #print(repr(len(english_words)))
