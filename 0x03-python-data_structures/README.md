__ALX HIGHER LEVEL PROGRAMMING__

_0x03-Python-Data-Structures_

     
# Requirements
## Python Scripts

*    Allowed editors: *vi, vim, emacs*
*    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*    All your files should end with a new line
*    The first line of all your files should be exactly *#!/usr/bin/python3*
*    A *README.md* file, at the root of the folder of the project, is mandatory
*    Your code should use the pycodestyle (version 2.7.\*)
*    All your files must be executable
*    The length of your files will be tested using *wc*

## C

*    Allowed editors: *vi, vim, emacs*
*    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
*    All your files should end with a new line
*    Your code should use the *Betty* style. It will be checked using *betty-style.pl* and *betty-doc.pl*
*    You are not allowed to use global variables
*    No more than 5 functions per file
*    In the following examples, the *main.c* files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own *main.c* files at compilation. Our *main.c* files might be different from the one shown in the examples
*    The prototypes of all your functions should be included in your header file called *lists.h*
*    Don’t forget to push your header file
*    All your header files should be include guarded

# Tasks

## Mandatory

### 0. Print a list of integers

Write a function that prints all integers of a list.
* Prototype: *def print_list_integer(my_list=[]):*


### 1. Secure access to an element in a list

Write a function that retrieves an element from a list like in C.
* Prototype: *def element_at(my_list, idx):*


### 2. Replace element

Write a function that replaces an element of a list at a specific position (like in C).

*    Prototype: *def replace_in_list(my_list, idx, element):*


### 3. Print a list of integers... in reverse!

Write a function that prints all integers of a list, in reverse order.

*    Prototype: *def print_reversed_list_integer(my_list=[]):*


### 4. Replace in a copy

Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

*    Prototype: *def new_in_list(my_list, idx, element):*


### 5. Can you C me now?

Write a function that removes all characters *c* and *C* from a string.

*    Prototype: *def no_c(my_string):*


### 6. Lists of lists = Matrix

Write a function that prints a matrix of integers.

 *   Prototype: *def print_matrix_integer(matrix=[[]]):*


### 7. Tuples addition

Write a function that adds 2 tuples.

*    Prototype: *def add_tuple(tuple_a=(), tuple_b=()):*


### 8. More returns!

Write a function that returns a tuple with the length of a string and its first character.

*    Prototype: *def multiple_returns(sentence):*


### 9. Find the max

Write a function that finds the biggest integer of a list.

*    Prototype: *def max_integer(my_list=[]):*


### 10. Only by 2

Write a function that finds all multiples of 2 in a list.

*    Prototype: *def divisible_by_2(my_list=[]):*


### 11. Delete at

Write a function that deletes the item at a specific position in a list.

*    Prototype: *def delete_at(my_list=[], idx=0):*


### 12. Switch


Complete the source code in order to switch value of *a* and *b*

*    You can find the source code [here](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py)
*    Your code should be inserted where the comment is (line 4)
*    Your program should be exactly 5 lines long


### 13. Linked list palindrome

**Technical interview preparation:**

*    You are not allowed to google anything
*    Whiteboard first\

Write a function in C that checks if a singly linked list is a palindrome.

*    Prototype: *int is_palindrome(listint_t **head);*
*    Return: 0 if it is not a palindrome, 1 if it is a palindrome
*    An empty list is considered a palindrome

## Advanced

### 14. CPython #0: Python lists

CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.\
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.

*    All your files will be interpreted/compiled on Ubuntu 14.04 LTS \



Create a C function that prints some basic info about Python lists.

*    Prototype: *void print_python_list_info(PyObject \*p);*
*    Format: see example
*    Python version: 3.4
*    Your shared library will be compiled with this command line: *gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c*
*    OS: *Ubuntu 14.04 LTS*
*    Start by reading:
	*	listobject.h
	*	object.h
	*	[Common Object Structures](https://docs.python.org/3.4/c-api/structures.html)
	*	[List Objects](https://docs.python.org/3.4/c-api/list.html)
```
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
julien@ubuntu:~/CPython$ cat 100-test_lists.py 
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
julien@ubuntu:~/CPython$ python3 100-test_lists.py 
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
julien@CPython:~/CPython$

```
