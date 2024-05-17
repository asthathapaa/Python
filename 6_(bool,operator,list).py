Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=5
if (a>b):
    print("a is g")
    else:
        
SyntaxError: invalid syntax
if (a>b):
    print("a is g")
    
    else:
        
SyntaxError: invalid syntax
if (a>b):
    print("a is g")

else:
    print("b is g")

    
a is g
print(bool("hello"))
True
print(bool(15))
True
print("abc")
abc
bool("abc")
True
bool(123)
True
bool(abc)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    bool(abc)
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?
print(bool(False))
False
print(bool())
False

class myclass():
    def__len__(self):
        
SyntaxError: invalid syntax
class myclass():
 def__len__(self):
     
SyntaxError: invalid syntax
class myclass():
 def __len__(self):
     return 0
myob= myclass()
SyntaxError: invalid syntax
class myclass():
 def __len__(self):
     return 0
    
myob= myclass()
SyntaxError: invalid syntax
class myclass():
 def __len__(self):
     return 0

 myob = myclass()
 print(bool(myob))

 
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    class myclass():
  File "<pyshell#28>", line 5, in myclass
    myob = myclass()
NameError: name 'myclass' is not defined
class myclass():
 def __len__(self):
     return 0

    
myob= myclass()
print(bool(myob))
False
def myfun():
    return true

print(myfun())
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(myfun())
  File "<pyshell#35>", line 2, in myfun
    return true
NameError: name 'true' is not defined. Did you mean: 'True'?
def myfun():
    return true

print(myfun())
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(myfun())
  File "<pyshell#38>", line 2, in myfun
    return true
NameError: name 'true' is not defined. Did you mean: 'True'?
def myfun():
    return true

print(myfun())
SyntaxError: invalid syntax
def myfun():
    return true

 print(myfun())
 
SyntaxError: unindent does not match any outer indentation level
def myfun():
    return true

  print(myfun())
  
SyntaxError: unindent does not match any outer indentation level
def myfun():
    return True

print(myfun())
True

def myFun():
    return True

if myFun():
    print("Yes!")
else:
    print("No")

    
Yes!
x= 200
print(isinstance(x,int))
True
print(5%3)
2
print(2**5)
32
print(2*2*2*2*2)
32
print(15 //2)
7

x =5
x -=3
print(x)
2
print( 5%=3)
SyntaxError: invalid syntax
print(5 %=3)
SyntaxError: invalid syntax
print(5 %= 3)
SyntaxError: invalid syntax
x =5
x %=3
print(x)
2
x=5
x **=3
print(x)
125
x=5
x >>= 3
print(x)
0
print(x := 3)
3
x = 5
y =3
print(x == y)
False
print(x !=3)
True
print(x>=y)
True

x = 5
print( x> 3 and x<10)
True

print(x>3 or x<10)
True

print(not(x>3 and x<10))
False

x=["apple","bannana"]
y=["apple","bannana"]

z=x
print(x is z)
True
print(x is y)
False
print(x == y)
True
print("banana" in x)
False
print("kiwi" in x)
False

print9 6 & 3)
SyntaxError: unmatched ')'

print(6 & 3)
2
print(6 | 3)
7
print(6 ^ 3)
5
print(~3)
-4
print(3<<6)
192
print(3>>6)
0
print((6+3) -(6+3))
0
print(100 + 5*3)
115
print(8 >>4-2)
2
print(5 ==4+1)
True
print9 not 4==4)
SyntaxError: unmatched ')'

print(not 4==4)
False
print(5+4-7+3)
5
thislist =["apple","banana","cherry"]
print(thislist)
['apple', 'banana', 'cherry']
print(len(thislist))
3
list1=[1,2,3,5,8]
list2=[True,False,False]
print(list1,list2)
[1, 2, 3, 5, 8] [True, False, False]
print(type(list1))
<class 'list'>
print(thislist[1])
banana
print(thislist[-1])
cherry
this[1:3] =["bt","watermelon"]
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    this[1:3] =["bt","watermelon"]
NameError: name 'this' is not defined. Did you forget to import 'this'?
thislist[1:3] =["bt","watermelon"]
print(thislist)
['apple', 'bt', 'watermelon']
thislist.append("orange")
print(thislist)
['apple', 'bt', 'watermelon', 'orange']

thislist.extend(list1)
print(thislist)
['apple', 'bt', 'watermelon', 'orange', 1, 2, 3, 5, 8]
thislist.remove("orange")print(thislist)
SyntaxError: invalid syntax
thislist.remove("orange")
print(thislist)
['apple', 'bt', 'watermelon', 1, 2, 3, 5, 8]
thislist.clear()
print(thislist)
[]
for x in list1:
    print(x)

    
1
2
3
5
8
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

    
apple
banana
cherry
i=0
while i< len(thislist):
    print(thislist[i])
    i++
    
SyntaxError: invalid syntax
while i< len(thislist):
    print(thislist[i])
    i= i+1

    
apple
banana
cherry
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
KeyboardInterrupt
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[]

for x in fruits:
    if "a" in x:
        newlist.append(x)

        
print(newkist)
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    print(newkist)
NameError: name 'newkist' is not defined. Did you mean: 'newlist'?
>>> print(newlist)
['apple', 'banana', 'mango']
>>> 
>>> fruits =["apple","banna","cherry","kiwi"]
>>> newlist =[x for x in fruits if "a" in x]
>>> print(newlist)
['apple', 'banna']
>>> 
>>> fruits= ["apple","banna","ch"]
>>> newlist= [x for x in fruits if "a" in x]
>>> print(newlist)
['apple', 'banna']
>>> fruits =["apple","banna","cherry","kiwi"]
>>> thislist.sort()
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> this=[100,50,65,82,23]
>>> this.sort(reverse=True)
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> mylist= thislist.copy()
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> ['apple', 'banana', 'cherry']
['apple', 'banana', 'cherry']
>>> 
>>> list1 = ["a", "b" , "c"]
>>> list2 = [1, 2, 3]
>>> 
>>> for x in list2:
...     list1.append(x)
... 
...     
>>> print(list1)
['a', 'b', 'c', 1, 2, 3]
>>> 
>>> fruits = ['apple', 'banana', 'cherry']
>>> fruits.reverse()
>>> print(fruits)
['cherry', 'banana', 'apple']
