Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x= (2<5 and 4>2)
>>> print(x)
True
>>> 
>>> import calender as c
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import calender as c
ModuleNotFoundError: No module named 'calender'
>>> import calendar as c
>>> print(c.month_name[1])
January
>>> print(c.day[4])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(c.day[4])
  File "C:\Users\User\AppData\Local\Programs\Python\Python312\Lib\calendar.py", line 54, in __getattr__
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
AttributeError: module 'calendar' has no attribute 'day'. Did you mean: 'Day'?
>>> 
>>> x= "hello"
>>> assert x== "hello"
>>> 
>>> assert x =="no"
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    assert x =="no"
AssertionError
>>> for i in range(10):
...     if i ==7:
...         break
...     print(i)
... 
...     
0
1
2
3
4
5
6
