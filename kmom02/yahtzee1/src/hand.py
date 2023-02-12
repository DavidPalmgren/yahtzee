#!/usr/bin/env python3
"""
Contains the hand class.
"""

from src.die import Die

class Hand:
    """This is the hand class"""

    def __init__(self, dice_values = None):
        """_hand init shit_"""
        self.dice = []
        if dice_values is None:
            for _ in range(5):
                self.dice.append(Die())
        else:
            self.dice = [Die(dice_values[0]), Die(dice_values[1]), Die(dice_values[2]),
                         Die(dice_values[3]), Die(dice_values[4])]

    def roll(self, indexes = None):
        """
        Rolls the die at index position taking from indexes:list n stuff.
        """
        if indexes is None:
            for x in range(5):
                self.dice[x] = Die()
        else:
            for x in indexes:
                self.dice[x] = Die()

    def __str__(self):
        return ', '.join([str(die.get_value()) for die in self.dice])
        #return str(self.dice).strip("[]")
