Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def fun(fname):
    print("First name"+fname)

    
fun("astha")
First nameastha
def fun(*kid):
    print("Middle"+kid[2]);

    
fun("as","ah","ak")
Middleak
def fun(*kid):
    print("Middle"+kid[1]);

    
fun("as","ah","ak")
Middleah
def my(k1,k2,k3)
SyntaxError: expected ':'
def my(k1,k2,k3):
    print("kids"+k3)

    
my(k1="as",k2="ab",k3="ak");
kidsak
def my(k1,k2,k3):
    print("kids= "+k3)

    
my(k1="as",k2="ab",k3="ak");
kids= ak
def fun(fname="astha"):
    print("First name"+fname)

    
fun()
First nameastha
def fun(fname="astha"):
    print("First name="+fname)

    
fun()
First name=astha
def fun(x):
    return 5*x

print(fun(10))
50
def fun():
    50
    pass


pass
def fun(x):
    print(x)

    
fun(x=10)
10
#recursion
def recur(k):
    if(k>0):
        res=k+recur(k-1)
        print(res)
        else
        
SyntaxError: invalid syntax
def recur(k):
    if(k>0):
        res=k+recur(k-1)
        print(res)
    else
    
SyntaxError: expected ':'
def recur(k):
    if(k>0):
        res=k+recur(k-1)
        print(res)
    else:
        re=0
        return res

    
print("example:)
      
SyntaxError: unterminated string literal (detected at line 1)
print("example:")
      
example:
recur(9)
      
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    recur(9)
  File "<pyshell#57>", line 3, in recur
    res=k+recur(k-1)
  File "<pyshell#57>", line 3, in recur
    res=k+recur(k-1)
  File "<pyshell#57>", line 3, in recur
    res=k+recur(k-1)
  [Previous line repeated 6 more times]
  File "<pyshell#57>", line 7, in recur
    return res
UnboundLocalError: cannot access local variable 'res' where it is not associated with a value
def recur(k):
    if(k>0):
        res=k+recur(k-1)
        print(res)
    else:
        res=0
        return res
    print("Example")

    
recur(5)
1
Example
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    recur(5)
  File "<pyshell#63>", line 3, in recur
    res=k+recur(k-1)
  File "<pyshell#63>", line 3, in recur
    res=k+recur(k-1)
  File "<pyshell#63>", line 3, in recur
    res=k+recur(k-1)
  [Previous line repeated 1 more time]
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
def recur(k):
    if(k>0):
        res=k+recur(k-1)
        print(res)
        return res
    else:
        res=0
        return res

    print("Example")

    
recur(7)
1
3
6
10
15
21
28
28
#lambda
x= lambda a:a+10
print(x(6))
16
def fun(n)
SyntaxError: expected ':'
def fun(n):
    return lambda a:a/n

fun(30)
<function fun.<locals>.<lambda> at 0x000002122F7842C0>
scooter= ["vespa","fascino","ntorq"]
for x in scooter:
    print(x)

    
vespa
fascino
ntorq
scooter.append("dio")
print(scooter)
['vespa', 'fascino', 'ntorq', 'dio']
for x in scooter:
    print(x)

    
vespa
fascino
ntorq
dio
scooter.pop(2)
'ntorq'
class My:
    x=5
    print(x)

    
5
print(My)
<class '__main__.My'>
class Pesn:
    def  __init__(self,n,a):
        self.n=n
        self.a=a

        
class Pesn:
    def  __init__(self,n,a):
        self.n=n
        self.a=a
    p1= Pesn("Jaz",45)

    
print(p1.n)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print(p1.n)
NameError: name 'p1' is not defined
class Pesn:
    def  __init__(self,n,a):
        self.n=n
        self.a=a


    p1= Pesn("Jaz",45)
    
SyntaxError: unexpected indent
>>> p1= Pesn("Jaz",45)
>>> print(p1.n)
Jaz
>>> print(p1.a)
45
>>> class Pesn:
...     def  __init__(self,n,a):
...         self.n=n
...         self.a=a
...     def __str__(self):
...         return f"{self.n}({self.age})"
... p1= Pesn("Jaz",45)
SyntaxError: invalid syntax
>>> class Pesn:
...     def  __init__(self,n,a):
...         self.n=n
...         self.a=a
...     def __str__(self):
...         return f"{self.n}({self.age})"
... 
...     
>>> p1= Pesn("Jaz",45)
>>> print(p1)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    print(p1)
  File "<pyshell#111>", line 6, in __str__
    return f"{self.n}({self.age})"
AttributeError: 'Pesn' object has no attribute 'age'
>>> class Pesn:
...     def  __init__(self,n,a):
...         self.n=n
...         self.a=a
...     def __str__(self):
...         return f"{self.n}({self.a})"
... 
...     
>>> p1= Pesn("Jaz",45)
>>> print(p1)
Jaz(45)
