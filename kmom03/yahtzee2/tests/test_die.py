#!/usr/bin/env python3
""" Module for testing the class Die """

import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_no_args(self):
        """constructor without arg works..."""
        die = Die()
        self.assertTrue(die) #check if exists

    def test_with_args(self):
        """constructor with arg works..."""
        die = Die(5)
        self.assertEqual(die.get_value(), 5) #checks private value

    def test_with_invalid_args(self):
        """ if invalid number instance is called it will set between 1-6 """
        die = Die(13)
        self.assertTrue(1 <= die.get_value() <= 6) #check if betweeen 1 and 6 and or is 1 or 6

    def test_roll_new_val(self):
        """roll returns new value..."""
        random.seed(10)
        die = Die()
        #die._value = 5
        value = die.roll()
        self.assertEqual(value, 1)

    def test_get_name(self):
        """get name fungerar returnerar "five" """
        random.seed(10)
        die = Die()
        self.assertEqual(die.get_name(),"five")

    def test_str(self):
        """str of die(5) equals "5" """
        die = Die(5)
        self.assertEqual(str(die), "5")

    def test__eq__(self):
        """die(5)=die(5) and die(4)!=die(5)"""
        die1 = Die(4)
        die2 = Die(5)
        self.assertFalse(die1 == die2)

        die1 = Die(5)
        die2 = Die(5)
        self.assertTrue(die1 == die2)
        