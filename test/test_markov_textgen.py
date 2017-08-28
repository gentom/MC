#!/usr/bin/env python
# coding: utf-8
import sys
import os
sys.path.append(os.pardir)
from mc import markov_textgen

input_file = open('./data/test_markov_textgen.txt')
markov = markov_textgen.MarkovText(input_file)
print(markov.text_generator())