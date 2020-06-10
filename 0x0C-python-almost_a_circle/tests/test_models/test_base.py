#!/usr/bin/python3
"""
Unittest por Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Runs tests on the Base class
    """

    def test_without_arg(self):
        """ Test what happens when no arguments are passed
        """

        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)

    def test_with_arg(self):
        """ Test that id is being assigned correctly
        """

        Base._Base__nb_objects = 0
        b = Base(50)
        self.assertEqual(b.id, 50)

    def test_multiple_instances(self):
        """ Test if id is correct after multiple instances
        """

        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()

        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

if __name__ == '__main__':
    unittest.main()

    def test_reassign_id(self):
        """ Test if id is correct in all instances after reassigning it
        """

        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()

        instances = [b1, b2, b3, b4]
        position = 0

        for i in range(100, 500, 100):
            instances[position].id = i
            self.assertEqual(instances[position].id, i)
            position += 1

