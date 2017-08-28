#!/usr/bin/env python
# coding: utf-8
from random import randint, random, choice

class MarkovText:
		def __init__(self, input_file, chain_size=3):
			self.chain_size = chain_size
			self.cache = {}
			self.input_file = input_file
			self.words = self.file2words()
			self.word_size = len(self.words)
			self.database()
		

		def file2words(self):
			self.input_file.seek(0)
			data = self.input_file.read()
			words = data.split()
			return words

		def words_at_position(self, i):
			chain = []
			for chain_index in range(0, self.chain_size):
				chain.append(self.words[i + chain_index])
			return chain

		def chain(self):

			if len(self.words) < self.chain_size:
				return

			for i in range(len(self.words) - self.chain_size - 1):
				yield tuple(self.words_at_position(i))

		def database(self):
			for chain_set in self.chain():
				key = chain_set[:self.chain_size - 1]
				next_word = chain_set[-1]
				if key in self.cache:
					self.cache[key].append(next_word)
				else:
					self.cache[key] = [next_word]

		def text_generator(self, size=25):
			seed = randint(0, self.word_size - 3)
			gen_words = []
			seed_words = self.words_at_position(seed)[:-1]
			gen_words.extend(seed_words)
			for i in range(size):
				last_word_len = self.chain_size - 1
				last_words = gen_words[-1 * last_word_len:]
				next_word = choice(self.cache[tuple(last_words)])
				gen_words.append(next_word)
			return ' '.join(gen_words)