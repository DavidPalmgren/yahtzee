#!/usr/bin/env python3
"""
Contains the die class.
"""

import random

class Die():
    """ Die class that handles dies with model and price. """
    MIN_ROLL_VALUE = 1
    MAX_ROLL_VALUE = 6

    def __init__(self, value = None):
        """ Constuctor """
        if value is None:
            self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        elif value < self.MIN_ROLL_VALUE:
            self._value = self.MIN_ROLL_VALUE
        elif value > self.MAX_ROLL_VALUE:
            self._value = self.MAX_ROLL_VALUE
        else:
            self._value = value

    def get_name(self, indiv = None):
        """ Returns a SOMETHING representing the value of the die """
        die_names = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
        }
        if indiv is not None:
            return die_names[indiv]
        if hasattr(self, 'self.value'):
            return die_names[self.value] ##dont mind this
        return die_names[self._value]

    def get_value(self):
        """returns le self value"""
        return self._value

    def roll(self):
        """ roll the die lego"""
        self._value = random.randint(self.MIN_ROLL_VALUE, self.MAX_ROLL_VALUE)
        return self._value # ? såhär eller det äns mening me de?

    def __str__(self):
        return f"{self.get_value()}"
