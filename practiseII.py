Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
color_list = ["Red","Green","White" ,"Black"]
color_list = ["Red","Green","White" ,"Black"]
print(color_list(0))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(color_list(0))
TypeError: 'list' object is not callable
print(color_list[0])
Red
print("%s%s"%(color_list[0],color_list[3]))
RedBlack
print("%s %s"%(color_list[0],color_list[3]))
Red Black
exam_st_date = (11, 12, 2014)
print("Day /month /year %i / %i / %i" (exam_st_date[0],exam_st_date[1],exam_st_date[2]))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("Day /month /year %i / %i / %i" (exam_st_date[0],exam_st_date[1],exam_st_date[2]))
TypeError: 'str' object is not callable
print("%i / %i / %i" (exam_st_date[0],exam_st_date[1],exam_st_date[2]))
Traceback (most recent call last):

  File "<pyshell#10>", line 1, in <module>
    print("%i / %i / %i" (exam_st_date[0],exam_st_date[1],exam_st_date[2]))
TypeError: 'str' object is not callable
print("%i / %i / %i" %(exam_st_date[0],exam_st_date[1],exam_st_date[2]))
11 / 12 / 2014
print("Day /month /year %i / %i / %i" %(exam_st_date[0],exam_st_date[1],exam_st_date[2]))
Day /month /year 11 / 12 / 2014
print("Day month year : %i / %i / %i" %(exam_st_date[0],exam_st_date[1],exam_st_date[2]))
Day month year : 11 / 12 / 2014
itgr = input("The value of n","%s")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    itgr = input("The value of n","%s")
TypeError: input expected at most 1 argument, got 2
itgr = input("The value of n :")
The value of n :5
print("The result:",itgr+itgr+itgr)
The result: 555
itg = int(input("Enter integer :"))
Enter integer :
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    itg = int(input("Enter integer :"))
ValueError: invalid literal for int() with base 10: ''
Enter integer :5
SyntaxError: invalid syntax
itg = int(input("Enter integer :"))
Enter integer :5
n1 = int("%s" %a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    n1 = int("%s" %a)
NameError: name 'a' is not defined
print("%i / %i / %i" (exam_st_date[0],exam_st_date[1],exam_st_date[2]))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print("%i / %i / %i" (exam_st_date[0],exam_st_date[1],exam_st_date[2]))
TypeError: 'str' object is not callable
itg = int(input("Enter integer :")) \
      one = int("%s",itg)
SyntaxError: invalid syntax
itg = int(input("Enter integer :")) \one = int("%s",itg)
SyntaxError: unexpected character after line continuation character
itg = int(input("Enter integer :")) \                                                   one = int("%s",itg)
SyntaxError: unexpected character after line continuation character
itg = int(input("Enter integer :"))+ \                                                   one = int("%s",itg)+\
      
SyntaxError: unexpected character after line continuation character
itg = int(input("Enter integer :"))+ \                                                   one = int("%s",itg) \
      
SyntaxError: unexpected character after line continuation character
itg = int(input("Enter integer :"))+ \                                                   one = int("%s",itg)
SyntaxError: unexpected character after line continuation character
itg = int(input("Enter integer :"))+ \                                                   one = int("%s",itg)
SyntaxError: unexpected character after line continuation character
itg = int(input("Enter integer :"))                                                     one = int("%s",itg)
SyntaxError: invalid syntax
itg = int(input("Enter integer :"));                                                    one = int(itg)
Enter integer :5
two = int(itg,itg)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    two = int(itg,itg)
TypeError: int() can't convert non-string with explicit base
The result: 555
SyntaxError: invalid syntax
itg = int(input("Enter integer :"));                                                     one = int("%s" %itg)
Enter integer :6
two = int("%s %s" %(itg,itg))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    two = int("%s %s" %(itg,itg))
ValueError: invalid literal for int() with base 10: '6 6'
a = int(input("Input an integer: "))

# Create new integers 'n1', 'n2', and 'n3' by concatenating 'a' with itself one, two, and three times, respectively
n1 = int("%s" % a)          # Convert 'a' to an integer
n2 = int("%s%s" % (a, a))   # Concatenate 'a' with itself and convert to an integer
n3 = int("%s%s%s" % (a, a, a))  # Concatenate 'a' with itself twice and convert to an integer

# Calculate the sum of 'n1', 'n2', and 'n3' and print the result
print(n1 + n2 + n3)
SyntaxError: multiple statements found while compiling a single statement
a = int(input("Input an integer: "))

# Create new integers 'n1', 'n2', and 'n3' by concatenating 'a' with itself one, two, and three times, respectively
n1 = int("%s" % a)          # Convert 'a' to an integer
n2 = int("%s%s" % (a, a))   # Concatenate 'a' with itself and convert to an integer
n3 = int("%s%s%s" % (a, a, a))  # Concatenate 'a' with itself twice and convert to an integer

# Calculate the sum of 'n1', 'n2', and 'n3' and print the result
print(n1 + n2 + n3)
SyntaxError: multiple statements found while compiling a single statement
a = int(input("Input an integer: "))

# Create new integers 'n1', 'n2', and 'n3' by concatenating 'a' with itself one, two, and three times, respectively
... n1 = int("%s" % a)          # Convert 'a' to an integer
... n2 = int("%s%s" % (a, a))   # Concatenate 'a' with itself and convert to an integer
... n3 = int("%s%s%s" % (a, a, a))  # Concatenate 'a' with itself twice and convert to an integer
... 
... # Calculate the sum of 'n1', 'n2', and 'n3' and print the result
... print(n1 + n2 + n3)
SyntaxError: multiple statements found while compiling a single statement
>>> a = int(input("Input an integer: "));
Input an integer: 
============= RESTART: C:/Users/LENOVO/OneDrive/Desktop/python/practise.py =============
Input an integer: 7
Traceback (most recent call last):
  File "C:/Users/LENOVO/OneDrive/Desktop/python/practise.py", line 3, in <module>
    n2 = int("%s %s" %(a,a))
ValueError: invalid literal for int() with base 10: '7 7'
>>> 
============= RESTART: C:/Users/LENOVO/OneDrive/Desktop/python/practise.py =============
Input an integer: 8
Traceback (most recent call last):
  File "C:/Users/LENOVO/OneDrive/Desktop/python/practise.py", line 3, in <module>
    n2 = int("%s %s" % (a,a))
ValueError: invalid literal for int() with base 10: '8 8'
>>> 
============= RESTART: C:/Users/LENOVO/OneDrive/Desktop/python/practise.py =============
Input an integer: 4
492
>>> 
============= RESTART: C:/Users/LENOVO/OneDrive/Desktop/python/practise.py =============
Input an integer: 5
615
>>> 
============= RESTART: C:/Users/LENOVO/OneDrive/Desktop/python/practise.py =============
Input an integer: 5
5 55 555
615
>>> print(abs.__doc__)
Return the absolute value of the argument.
>>> print(len.__doc__)
Return the number of items in a container.
>>> print(sum.__doc__)
Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may
reject non-numeric types.
