#!/usr/bin/env python3
""" Module for testing the class Hand """

import unittest
import random
from src.die import Die
from src.hand import Hand

class TestHand(unittest.TestCase):
    """tests for class Hand"""

    def test_no_args_hand(self):
        """hand constructor without arg works..."""
        hand = Hand()
        self.assertTrue(hand) #check if exists

    def test_with_args_hand(self):
        """hand constructor with arg works..."""
        test_list = [5, 1, 3, 4, 5]
        hand = Hand(test_list)

        self.assertEqual(hand.to_list(), test_list) #checks private value
