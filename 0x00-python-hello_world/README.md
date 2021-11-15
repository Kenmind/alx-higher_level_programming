__ALX HIGHER LEVEL PROGRAMMING__

_0x00-Python-Hello_World_

# QUESTIONS/TASKS

## 0. Run Python file
Write a Shell script that runs a Python script.\
The Python file will be saved in the environment variable _$PYFILE_
```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
```
## 1. Run inline
Write a Shell script that runs Python code.\
The Python code will be saved in the environment variable _$PYCODE_.
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Best School: {}".format(88+10))'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
```
## 2. Hello, print
Write a Python script that prints exactly _"Programming is like a multilingual puzzle_, followed by a new line.
	* Use the function _print_
 ```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```
## 3. Print integer
  
Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable _number_, followed by _Batterystreet_, followed by a new line.

*    You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py)
*    The output of the script should be:
	* the number, followed by _Battery street_,
	* followed by a new line
*    You are not allowed to cast the variable number into a string
*    Your code must be 3 lines long
*    You have to use the new print numbers [tips](https://pyformat.info/#number) (with .format(...))
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```
    C is strongly typed… not in Python! The variable number can be assigned to a string, a float, a bool etc… Forcing the type during a string format ("...".format(...)) is a way to control the type of a variable

##4. Print float
  
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
* You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py)
* The output of the program should be:
	* Float:, followed by the float with only 2 digits
	* followed by a new line
* You are not allowed to cast number to string
* You have to use the new print formatting [tips](https://pyformat.info/#number_padding) (with .format(...))
```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$
```
