Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
10/2
5.0
10//2
5
4*2
8
4**2
16
name="python programming"
type(name)
<class 'str'>
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
help(name.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

name.count("p")
2
name.count("o")
2
name.count("o")
2
name.count("pro")
1
help(name.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

name.upper("p")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name.upper("p")
TypeError: str.upper() takes no arguments (1 given)
name.upper()
'PYTHON PROGRAMMING'
help(name.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

help(name.lower)
Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.

name.lower()
'python programming'
type(name)
<class 'str'>

len(name)
18
name[-18]
'p'
name[0]
'p'
name[18]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    name[18]
IndexError: string index out of range
name[17]
'g'
name[5]
'n'
name[0:2]
'py'
name[0::2]
'pto rgamn'
name[0:3]
'pyt'
name[0::3]
'ph oai'
name[0: ]
'python programming'
name[ :-1]
'python programmin'
name[1::6]
'ypm'
name[1::2]
'yhnpormig'
name[1:2]
'y'
name[0:1]
'p'
name[0:10:2]
'pto r'
name[::-1]
'gnimmargorp nohtyp'
name[::-2]
'gimropnhy'
>>> name[::-4]
'gmony'
>>> yes=True
>>> yes=False
>>> yes=done
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    yes=done
NameError: name 'done' is not defined. Did you mean: 'None'?
>>> name in "python"
False
>>> "p" in python
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    "p" in python
NameError: name 'python' is not defined
>>> "p"name in python
SyntaxError: invalid syntax
>>> help(in)
SyntaxError: invalid syntax
>>> "p" name in python
SyntaxError: invalid syntax
>>> 'p' name in
SyntaxError: invalid syntax
>>> 'p' in name
True
>>> 'o' in name
True
>>> "hee" not in name
True
>>> "hee" in name
False
>>> name="astha"
>>> name="astha"
>>> name is "astha"
True
>>> name is not"astha"
False
>>> name is "thapa"


