#!/usr/bin/python3
"""
Unittest por Base class
"""
import unittest
import json
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_create_one(self):
        """ Test if the create method works
        """

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        expected = "[Rectangle] (1) 1/0 - 3/5\n"

        print(r1)

        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2

        print(r2)

        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        self.assertEqual(capturedOutput1.getvalue(), expected)
        self.assertEqual(capturedOutput2.getvalue(), expected)

        sys.stdout = sys.__stdout__

    def test_load_from_file_one(self):
        """ Test if load_from_file works with Rectangle
        """

        Base._Base__nb_objects = 0

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1

        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_output:
            print(rect)

        expected = "[Rectangle] (1) 2/8 - 10/7\n"

        self.assertEqual(capturedOutput1.getvalue(), expected)

        os.remove("./Rectangle.json")
        sys.stdout = sys.__stdout__

    def test_load_from_file_two(self):
        """ Test when load_from_file accessing a file that doesn't exist
        """

        Base._Base__nb_objects = 0

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1

        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        list_rectangles_output = Rectangle.load_from_file()

        print(list_rectangles_output)

        self.assertEqual(capturedOutput1.getvalue(), "[]\n")

        sys.stdout = sys.__stdout__

    def test_load_from_file_three(self):
        """ Test if load_from_file works with Square
        """

        Base._Base__nb_objects = 0

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1

        s1 = Square(10, 7, 8)
        list_squares_input = [s1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        for squ in list_squares_output:
            print(squ)

        self.assertEqual(capturedOutput1.getvalue(), "[Square] (1) 7/8 - 10\n")

        os.remove("./Square.json")
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
