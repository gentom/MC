#!/usr/bin/env python
# coding: utf-8
from random import choice, randint, random

# Work In Progress.
class Chain:
    def __init__(self, sets, t_matrix, step):
        self.current = choice(sets)
