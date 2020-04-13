import sys
import os
import math

if __name__ == '__main__':

    # read in file
    f = open('english-words-235k.txt')
    lines = f.readlines() 
    words = []

    # process words
    for line in lines:
        word = line.strip()
        if len(word) >= 8:
            words.append(word.lower())

    # add words to anagram dict
    grams = {}
    for word in words:

        # sorting string into chars
        sorted_word = sorted(word)
        chars = "".join(sorted_word)

        # key is chars, value is list of anagrams
        if chars in grams:
            grams[chars].append(word)
        else:
            grams[chars] = [word]

    # sorting by size/length
    # length is string length, size is # of grams in a bucket
    for key in grams:
        length = len(key)
        size = len(grams[key])
        if size > 1:
            print("here's a gram")