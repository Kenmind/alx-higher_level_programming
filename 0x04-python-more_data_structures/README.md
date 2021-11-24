__ALX HIGHER LEVEL PROGRAMMING__

_0x04-Python-More_Data_Structures_

# Requirements
## General

* Allowed editors: *vi, vim, emacs*
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly *#!/usr/bin/python3*
* A *README.md* file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.\*)
* All your files must be executable
* The length of your files will be tested using *wc*



# Tasks
## Mandatory

### 0. Squared simple

Write a function that computes the square value of all integers of a matrix.

* Prototype: *def square_matrix_simple(matrix=[]):*

### 1. Search and replace

Write a function that replaces all occurrences of an element by another in a new list.

* Prototype: *def search_replace(my_list, search, replace):*


### 2. Unique addition

Write a function that adds all unique integers in a list (only once for each integer).

* Prototype: *def uniq_add(my_list=[]):*


### 3. Present in both

Write a function that returns a set of common elements in two sets.

* Prototype: *def common_elements(set_1, set_2):*


### 4. Only differents

Write a function that returns a set of all elements present in only one set.

* Prototype: *def only_diff_elements(set_1, set_2):*


### 5. Number of keys

Write a function that returns the number of keys in a dictionary.

* Prototype: *def number_keys(a_dictionary):*



### 6. Print sorted dictionary

Write a function that prints a dictionary by ordered keys.

* Prototype: *def print_sorted_dictionary(a_dictionary):*



### 7. Update dictionary

Write a function that replaces or adds key/value in a dictionary.

* Prototype: *def update_dictionary(a_dictionary, key, value):*


### 8. Simple delete by key

Write a function that deletes a key in a dictionary.

* Prototype: *def simple_delete(a_dictionary, key=""):*



### 9. Multiply by 2

Write a function that returns a new dictionary with all values multiplied by 2

* Prototype: *def multiply_by_2(a_dictionary):*



### 10. Best score

Write a function that returns a key with the biggest integer value.

* Prototype: *def best_score(a_dictionary):*


### 11. Multiply by using map

Write a function that returns a list with all values multiplied by a number without using any loops.

* Prototype: *def multiply_list_map(my_list=[], number=0):*


### 12. Roman to Integer

**Technical interview preparation:**

* You are not allowed to google anything
* Whiteboard first

Create a function *def roman_to_int(roman_string):* that converts a [Roman numeral](https://alx-intranet.hbtn.io/rltoken/oSuwqUrL0BL_hi4VqVvs_g) to an integer.

* You can assume the number will be between 1 to 3999.
* *def roman_to_int(roman_string)* must return an integer
* If the *roman_string* is not a string or *None*, return 0
```
guillaume@ubuntu:~/0x04$ cat 12-main.py
#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

guillaume@ubuntu:~/0x04$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
guillaume@ubuntu:~/0x04$ 
```

## Advanced

### 13. Weighted average!

Write a function that returns the weighted average of all integers tuple *(<score>, <weight>)*

* Prototype: *def weight_average(my_list=[]):*


### 14. Squared by using map

Write a function that computes the square value of all integers of a matrix using *map*

* Prototype: *def square_matrix_map(matrix=[]):*


### 15. Delete by value

Write a function that deletes keys with a specific value in a dictionary.

* Prototype: *def complex_delete(a_dictionary, value):*


### 16. CPython #1: PyBytesObject

Create two C functions that print some basic info about Python lists and Python bytes objects.


Python lists:

* Prototype: *void print_python_list(PyObject \*p);*
* Format: see example

Python bytes:

* Prototype: *void print_python_bytes(PyObject \*p);*
* Format: see example
* Line “first X bytes”: print a maximum of 10 bytes
* If *p* is not a valid *PyBytesObject*, print an error message (see example)
* Read */usr/include/python3.4/bytesobject.h*

About:

* Python version: 3.4
* Your shared library will be compiled with this command line: *gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c*
* You are not allowed to use the following macros/functions:
	* Py\_SIZE
	* Py\_TYPE
	* PyList\_GetItem
	* PyBytes\_AS\_STRING
	* PyBytes\_GET\_SIZE
```
julien@ubuntu:~/CPython$ python3 --version
Python 3.4.3
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
julien@ubuntu:~/CPython$ cat 103-tests.py 
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s);
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
lib.print_python_bytes(b);
b = b'What does the \'b\' character do in front of a string literal?';
lib.print_python_bytes(b);
l = [b'Hello', b'World']
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(l)
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_python_list(l)
l = ["Holberton"]
lib.print_python_list(l)
lib.print_python_bytes(l);
julien@ubuntu:~/CPython$ python3 103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: �
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: Holberton
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
julien@ubuntu:~/CPython$ 
```
