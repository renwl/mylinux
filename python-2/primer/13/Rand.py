
from random import choice

class Rand(object):
    def _init_(self,seq):
        self.data = seq
    def _iter_(self):
        return self
    def __next__(self):
        return choice(self.data)
