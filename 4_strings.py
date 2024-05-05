Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x= int(1)
>>> print(x)
1
>>> y=int(2.8)
>>> z=int("3")
>>> print(y,z)
2 3
>>> z= string("3")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    z= string("3")
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> x=float(1)
>>> y=float(2.8)
>>> z=float("3")
>>> w=float("4.2")
>>> print(x,y,z,w)
1.0 2.8 3.0 4.2
>>> e=float("2.44")
>>> print(e)
2.44
>>> a=str("1")
>>> y=str(2)
>>> d=str(3.0)
>>> print(a,y,d)
1 2 3.0
>>> #STRING
>>> 
>>> print("HELLO")
HELLO
>>> A=print("helloo")
helloo
>>> a="hello"
>>> print(a)
hello
>>> a="hello, world"
>>> print(a[1])
e
>>> for x in "apple"
SyntaxError: expected ':'
>>> for x in "apple":
...     print(x)

    
a
p
p
l
e
print(len(x))
1
alphabet= "a b c d e"
print("a" in alphabet)
True
if "b" in alphabet:
    print("yes, 'b' is present")

    
yes, 'b' is present
print("f" not in alphabet)
True
print("g" in alphabet)
False
b= "Hello,World!"
print(b[1:5])
ello
print(b[0:6])
Hello,
print(b[2:])
llo,World!
print(b[5:])
,World!
print(b[-5:-2])
orl
print(b.upper())
HELLO,WORLD!
print(b.lower())
hello,world!
print(b.strip())
Hello,World!
print(a.replace("H","O"))
hello, world
print(b.replace("H","l"))
lello,World!
print(b.split(","))
['Hello', 'World!']
print(b.split("!"))
['Hello,World', '']
a="Astha"
b="Thapa"
print(a+b)
AsthaThapa
print(a+ b)
AsthaThapa
print(a+""+b)
AsthaThapa
c=a + "" +b
print(c)
AsthaThapa
print(a+" "+b)
Astha Thapa
age= 11
print("My name is xx and I'AM "+age)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print("My name is xx and I'AM "+age)
TypeError: can only concatenate str (not "int") to str
age="11"
print("age"+age)
age11
print("Age"+" "+age)
Age 11
price=59
txt=f"The price is {price} dollars"
print(txt)
The price is 59 dollars
