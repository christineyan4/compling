import sys
import os
import math

def process_file():
    f = open('english-words-235k.txt')
    lines = f.readlines() 
    words = []

    # process words
    for line in lines:
        word = line.strip()
        if len(word) >= 8:
            words.append(word.lower())
    
    return words

def is_unique(anagrams, word):
    for gram in anagrams:
        if gram == word:
            return False
    return True

def hash_words(words):
    grams = {}
    for word in words:

        # sorting string into chars
        sorted_word = sorted(word)
        chars = "".join(sorted_word)

        # add word as anagram if unique
        if chars in grams:
            anagrams = grams[chars]
            if is_unique(anagrams, word):
                anagrams.append(word)
        else:
            grams[chars] = [word]

    return grams

def build_sorted_dicts(grams):
    nested_grams = {}

    # building nested dicts, first by size, then by length
    for key in grams:
        size = len(grams[key])
        length = len(key)
        if size > 1:
            if size in nested_grams:
                length_dict = nested_grams[size]
                if length in length_dict:
                    grams_dict = length_dict[length]
                    grams_dict[key] = grams[key]
                else:
                    length_dict[length] = {key: grams[key]}
            else:
                nested_grams[size] = {length: {key: grams[key]}}

    # sorting nested_grams
    for size in nested_grams:
        length_dict = nested_grams[size]
        nested_grams[size] = dict(sorted(length_dict.items()))
    sorted_grams = dict(sorted(nested_grams.items()))

    return sorted_grams

def print_table(sorted_grams):
    for size in sorted_grams:
        print("Anagrams of size " + str(size)) 
        length_dict = sorted_grams[size]
        for length in length_dict:
            print("Anagrams of length " + str(length))
            grams = length_dict[length]
            for key in grams:
                print_string = ""
                for gram in grams[key]:
                    print_string += gram + " "
                print(print_string)

if __name__ == '__main__':

    # read in file
    words = process_file()

    # add unique words to anagram dict
    grams = hash_words(words)

    # build nested dicts sorted by size, then length 
    sorted_grams = build_sorted_dicts(grams)

    # output
    print_table(sorted_grams)