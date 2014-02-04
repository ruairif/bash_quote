#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bash_quote
----------------------------------

Tests for `bash_quote` module.
"""

import unittest

from bash_quote import bash_quote


class TestBash_quote(unittest.TestCase):

    def setUp(self):
        pass

    def test_number_of_quotes(self):
        info, quotes = bash_quote.get_quotes()
        self.assertEqual(50, len(info), len(quotes))
        info, quotes = bash_quote.get_quotes(option='r', num_quotes=50)
        self.assertEqual(50, len(info), len(quotes))
        info, quotes = bash_quote.get_quotes(option='l', num_quotes=50)
        self.assertEqual(50, len(info), len(quotes))
        info, quotes = bash_quote.get_quotes(option='t', num_quotes=100)
        self.assertEqual(100, len(info), len(quotes))

    def test_quotes_not_null(self):
        info, quotes = bash_quote.get_quotes()
        self.assertTrue(info[0], quotes[0])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
