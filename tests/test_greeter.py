# tests/test_greeter.py

import unittest
from src.greeter import say_hello, get_greeting

class TestGreeter(unittest.TestCase):

    def test_say_hello_default(self):
        self.assertEqual(say_hello("Alice"), "Hello, Alice!")

    def test_say_hello_spanish(self):
        self.assertEqual(say_hello("Bob", "es"), "Hola, Bob!")

    def test_get_greeting_english(self):
        self.assertEqual(get_greeting("en"), "Hello")
        
    def test_empty_name(self):
        self.assertEqual(say_hello(""), "Error: Name cannot be empty.")