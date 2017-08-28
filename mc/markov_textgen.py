#!/usr/bin/env python
# coding: utf-8
from random import randint, random, choice

class MarkovText:
    def __init__(self, input_file):
        self.cache = {}
        self.input_file = input_file
        self.words = self.file2words()
        self.word_size = len(self.words)
        self.database()

    def file2words(self):
        self.input_file.seek(0)
        data = self.input_file.read()

    def split2triples(self):
        if len(self.words) < 3:
            return
        for i in range(len(self.words)-2):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    def database(self):
        for w1, w2, w3 in self.split2triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = w3

    def text_generator(self, size=25):
        seed = randint(0, self.word_size-3)
        seed_word, next_word = self.words[seed], self.words[seed+1]
        w1, w2 = seed_word, next_word
        generating_words = []
        for i in range(size):
            generating_words.append(w1)
            w1, w2 = w2, choice(self.cache[(w1,w2)])
        generating_words.append(w2)
        return ' '.join(generating_words)