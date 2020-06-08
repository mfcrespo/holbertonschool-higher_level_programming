# **0x0B. Python - Input/Output**

## **Learning Objectives**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### **General**
+ Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
+ How to open a file
+ How to write text in a file
+ How to read the full content of a file
+ How to read a file line by line
+ How to move the cursor in a file
+ How to make sure a file is closed after using it
+ What is and how to use the with statement
+ What is JSON
+ What is serialization
+ What is deserialization
+ How to convert a Python data structure to a JSON string
+ How to convert a JSON string to a Python data structure

## **Requirements**

### **Python Scripts**
+ Allowed editors: vi, vim, emacs
+ All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
+ All your files should end with a new line
+ The first line of all your files should be exactly #!/usr/bin/python3
+ A README.md file at the root of the holbertonschool-higher_level_programming repo, containing a description of the repository
+ A README.md file, at the root of the folder of this project, is mandatory
+ Your code should use the PEP 8 style (version 1.7.*)
+ All your files must be executable
+ The length of your files will be tested using wc

### **Python Test Cases**
+ Allowed editors: vi, vim, emacs
+ All your files should end with a new line
+ All your test files should be inside a folder tests
+ All your test files should be text files (extension: .txt)
+ All your tests should be executed by using this command: python3 -m doctest ./tests/*
+ All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
+ All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
+ All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
+ We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# **Tasks**

0. Read file: Write a function that reads a text file (UTF8) and prints it to stdout	

1. Number of lines: Write a function that returns the number of lines of a text file

2. Read n lines: Write a function that reads n lines of a text file (UTF8) and prints it to stdout

3. Write to a file: Write a function that writes a string to a text file (UTF8) and returns the number of characters written

4. Append to a file: Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added

5. To JSON string: Write a function that returns the JSON representation of an object (string).

6. From JSON string to Object: Write a function that returns an object (Python data structure) represented by a JSON string

7. Save Object to a file: Write a function that writes an Object to a text file, using a JSON representation

8. Create object from a JSON file: Write a function that creates an Object from a “JSON file”

9. Load, add, save: Write a script that adds all arguments to a Python list, and then save them to a file

10. Class to JSON: Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object

11. Student to JSON: Write a class Student that defines a student by:

* Public instance attributes:
	+ first_name
	+ clast_name
	+ age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
* Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)
* You are not allowed to import any module

12. Student to JSON with filter: Write a class Student that defines a student by: (based on 11-student.py)

* Public instance attributes:
	+ first_name
	+ last_name
	+ age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
* Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):
	+ If attrs is a list of strings, only attribute names contained in this list must be retrieved.
	+ Otherwise, all attributes must be retrieved
* You are not allowed to import any module

13. Student to disk and reload: Write a class Student that defines a student by: (based on 12-student.py)

* Public instance attributes:
	+ first_name
	+ last_name
	+ age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
* Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):
	+ If attrs is a list of strings, only attributes name contain in this list must be retrieved.
	+ Otherwise, all attributes must be retrieved
* Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
	+ You can assume json will always be a dictionary
	+ A dictionary key will be the public attribute name
	+ A dictionary value will be the value of the public attribute
* You are not allowed to import any module

14. Pascal's Triangle: Technical interview preparation:

* You are not allowed to google anything
* Whiteboard first
* Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

	+ Returns an empty list if n <= 0
	+ You can assume n will be always an integer
