# **0x0A. Python - Inheritance**

## **Learning Objectives**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### **General**
+ Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
+ What is a superclass, baseclass or parentclass
+ What is a subclass
+ How to list all attributes and methods of a class or instance
+ When can an instance have new attributes
+ How to inherit class from another
+ How to define a class with multiple base classes
+ What is the default class every class inherit from
+ How to override a method or attribute inherited from the base class
+ Which attributes or methods are available by heritage to subclasses
+ What is the purpose of inheritance
+ What are, when and how to use isinstance, issubclass, type and super built-in functions

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

0. Lookup: Write a function that returns the list of available attributes and methods of an object:	

1. My list: Write a class MyList that inherits from list

2. Exact same object: Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

3. Same class or inherit from: Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

4. Only sub class of: Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

5. Geometry module: Write an empty class BaseGeometry.

6. Improve Geometry: Write a class BaseGeometry (based on 5-base_geometry.py).

7. Integer validator: Write a class BaseGeometry (based on 6-base_geometry.py).

8. Rectangle: Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

9. Full rectangle: Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

10. Square #1: Write a class Square that inherits from Rectangle (9-rectangle.py)

11. Square #2: Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
