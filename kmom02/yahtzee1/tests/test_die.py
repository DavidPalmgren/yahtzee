#!/usr/bin/env python3
""" Module for testing the class Car """

import unittest
import random
from src.die import Die

class TestDie(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_no_args(self):
        """_summary_"""
        die = Die()
        self.assertTrue(die) #check if exists

    def test_with_args(self):
        """_summary_"""
        die = Die(5)
        self.assertEqual(die.get_value(), 5) #checks private value

    def test_with_invalid_args(self):
        """_summary_"""
        die = Die(13)
        self.assertTrue(1 <= die.get_value() <= 6) #check if betweeen 1 and 6 and or is 1 or 6

    def test_roll_new_val(self):
        """_summary_"""
        random.seed(10)
        die = Die()
        #die._value = 5
        value = die.roll()
        self.assertEqual(value, 1)

    def test_get_name(self):
        """_summary_"""
        random.seed(10)
        die = Die()
        self.assertEqual(die.get_name(),"five")

    def test_str(self):
        """_summary_"""
        die = Die(5)
        self.assertEqual(str(die), "5")
