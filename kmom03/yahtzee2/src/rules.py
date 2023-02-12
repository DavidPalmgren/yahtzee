#!/usr/bin/env python3
"""
Contains the rules abstract class.
"""

from abc import ABC, abstractmethod
from src.hand import Hand

class Rule(ABC):
    """
    Abstrakta regel klassen
    """
    @abstractmethod
    def points(self, hand):
        """filler"""
        print("filler")
        pass

class SameValueRule(Rule):
    """
    kalkylerar värdet för de individuella klasserna
    """

    def __init__(self, value: int, name: str):
        self.name = name
        self.value = value

    def points(self, hand: Hand):
        total = 0
        for die in hand.dice:
            if die.get_value() == self.value:
                total += self.value
        return total

class Ones(SameValueRule):
    """
    Ones av samevaluerule av rule lol
    """
    def __init__(self):
        super().__init__(1, "Ones")

class Twos(SameValueRule):
    """
    Twos av samevaluerule av rule lol
    """
    def __init__(self):
        super().__init__(2, "Twos")

class Threes(SameValueRule):
    """
    Threes av samevaluerule av rule lol
    """
    def __init__(self):
        super().__init__(3, "Threes")

class Fours(SameValueRule):
    """
    Fours av samevaluerule av rule lol
    """
    def __init__(self):
        super().__init__(4, "Fours")

class Fives(SameValueRule):
    """
    Fives av samevaluerule av rule lol
    """
    def __init__(self):
        super().__init__(5, "Fives")

class Sixes(SameValueRule):
    """
    Sixes av samevaluerule av rule lol
    """
    def __init__(self):
        super().__init__(6, "Sixes")

class ThreeOfAKind(Rule):
    """Scoring rule Three Of A Kind"""
    def __init__(self):
        self.name = "Three Of A Kind"

    def points(self, hand: Hand):
        """
        Iterates through hand with get.value adds to list for value in list,
        if count(value) is 3 or more returns sum.
        """
        dice_values = [die.get_value() for die in hand.dice]
        for value in dice_values:
            if dice_values.count(value) >= 3:
                return sum(dice_values)
        return 0

class FourOfAKind(Rule):
    """Scoring rule Four Of A Kind"""
    def __init__(self):
        self.name = "Four Of A Kind"

    def points(self, hand: Hand):
        """
        Iterates through hand with get.value adds to list for value in list,
        if count(value) is 3 or more returns sum.
        """
        dice_values = [die.get_value() for die in hand.dice]
        for value in dice_values:
            if dice_values.count(value) >= 4:
                return sum(dice_values)
        return 0

class FullHouse(Rule):
    """Scoring rule Full House"""
    def __init__(self):
        self.name = "Full House"

    def points(self, hand: Hand):
        """
        check for 2 unique values and check count of val is 2/3 for kåk
        """
        dice_values = [die.get_value() for die in hand.dice]
        if len(set(dice_values)) == 2:
            for value in dice_values:
                if dice_values.count(value) in (2, 3):
                    return 25
        return 0

class SmallStraight(Rule):
    """Scoring rule SmallStraight"""
    def __init__(self):
        self.name = "Small Straight"

    def points(self, hand: Hand):
        """kollar att dicevalue indexen är sekventa och om allt ok ger 30p"""
        dice_values = [die.get_value() for die in hand.dice]
        dice_values.sort()
        dice_values = list(dict.fromkeys(dice_values))
        for i in range(len(dice_values) - 3):
            if (dice_values[i] == dice_values[i + 1] - 1 == dice_values[i + 2]
                - 2 == dice_values[i + 3] - 3):
                return 30
        return 0

class LargeStraight(Rule):
    """Scoring rule SmallStraight"""
    def __init__(self):
        self.name = "Large Straight"

    def points(self, hand: Hand):
        """kollar fall dem är i settet efter sort och bortagning av dubbletter"""
        dice_values = [die.get_value() for die in hand.dice]
        dice_values.sort()
        dice_values = list(dict.fromkeys(dice_values))
        if dice_values in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
            return 40
        return 0

class Yahtzee(Rule):
    """Scoring rule Yahtzee"""
    def __init__(self):
        self.name = "Yahtzee"

    def points(self, hand: Hand):
        """
        kollar att alla är samma värde och ger 50 om det de stämmer
        verkar som både set()och fromkeys funkar likvärdigt med att
        tabort duppletter iaf i detta fallet nicenice
        """
        dice_values = [die.get_value() for die in hand.dice]
        if len(set(dice_values)) == 1:
            return 50
        return 0

class Chance(Rule):
    """Scoring rule Chance"""
    def __init__(self):
        self.name = "Chance"

    def points(self, hand: Hand):
        """temp"""
        dice_values = [die.get_value() for die in hand.dice]
        return sum(dice_values)
