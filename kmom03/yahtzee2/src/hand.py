#!/usr/bin/env python3
"""
Contains the hand class.
"""
from typing import List
from src.die import Die

#jag har ändrat denna klassen för kmom03 hoppas det inte messar upp rättning av tidigare moment
class Hand:
    """This is the hand class"""

    def __init__(self, dice = None):
        """_hand init shit_"""

        if dice is None:
            self.dice = []
            for _ in range(5):
                self.dice.append(Die())
        else:
            self.dice = [Die(dice[0]), Die(dice[1]), Die(dice[2]),
                         Die(dice[3]), Die(dice[4])]

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

    def to_list(self):
        """
        itererar och gör en lista med get_value()
        """
        return [die.get_value() for die in self.dice]

    @staticmethod
    def from_list(dice_values: List[int]):
        print("dice_values")
        print(dice_values)
        hand = Hand(dice_values)
        print("handvalue")
        print(hand)
        return hand