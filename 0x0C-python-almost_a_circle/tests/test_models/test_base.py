#!/usr/bin/python3
"""
Unittest por Base class
"""
import unittest
import json
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

    def test_to_json_string(self):
        """ Test if the to_json_string method works
        """

        json_string = Base.to_json_string([{'x': 5}])
        json_string_two = Base.to_json_string([{'x': 5}, {'y': 3}])

        self.assertEqual(json_string, '[{"x": 5}]')
        self.assertEqual(json_string_two, '[{"x": 5}, {"y": 3}]')

    def test_to_json_string_none(self):
        """ Test what happens when to_json_string is passed None
        """

        json_string = Base.to_json_string(None)

        self.assertEqual(json_string, '[]')

    def test_to_json_string_empty_list(self):
        """ Test what happens when to_json_string is passed an empty list
        """

        json_string = Base.to_json_string([])

        self.assertEqual(json_string, '[]')

if __name__ == '__main__':
    unittest.main()
