Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=int(1)
print(x)
1
x= int(2.8)
print(x)
2
z= int("4")
print(z)
4
x= str("s1")
print(x)
s1
y=str(4)
z=str(9.0)
print(y,z)
4 9.0
print("astha"+" "+"thapa")
astha thapa
txt= "no double quote"inside" double quote"
SyntaxError: invalid syntax
w= 'It\'s alright.'
print(w)
It's alright.
txt='This will insert one \\(backlash).'
print(txt)
This will insert one \(backlash).
r="a \n b \n c\n d\n e\n"is will insert one \(backlash).
SyntaxError: invalid syntax
alpha="a \n b\n c\n"
print(alpha)
a 
 b
 c

p="a\nb\n"
print(p)
a
b

p="hello\rworld!"
print(p)
hello
world!
txt="hello \tworld";print(txt);
hello 	world
tst="h\bw";print(tst);
hw
x= "\110\145\153\154\157"
print(x)
Heklo
#string methods
txt="Tesla"
x= txt.isalpha()
print(x)
True
y=txt.center(20) print(y)
SyntaxError: invalid syntax
y=txt.center(20)
print(y)
       Tesla        
z=txt.isalnum()
print(z)
True




fruits=['apple','bannana','cherry']
fruits.append("orange")
print(fruits)
['apple', 'bannana', 'cherry', 'orange']
a=['a','b','c','d','e']
f=['g','h','i','j']
a.append(f)
print(a)
['a', 'b', 'c', 'd', 'e', ['g', 'h', 'i', 'j']]
fruits.clear()
print(fruits)
[]
x=a.copy()
print(x)
['a', 'b', 'c', 'd', 'e', ['g', 'h', 'i', 'j']]
x.count()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x.count()
TypeError: list.count() takes exactly one argument (0 given)
y=x.count()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    y=x.count()
TypeError: list.count() takes exactly one argument (0 given)
y=x.count("b")
print(y)
1
b=x.append("b")
y=b.count("b")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    y=b.count("b")
AttributeError: 'NoneType' object has no attribute 'count'
y=x.count("x")
print(y)
0
y=x.count("b")
print(y)
2
car=["ford","tesla","bmw"]
x.extends(cars)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    x.extends(cars)
AttributeError: 'list' object has no attribute 'extends'. Did you mean: 'extend'?
x.extend(car)
print(x)
['a', 'b', 'c', 'd', 'e', ['g', 'h', 'i', 'j'], 'b', 'ford', 'tesla', 'bmw']
x.reverse()
print(x)
['bmw', 'tesla', 'ford', 'b', ['g', 'h', 'i', 'j'], 'e', 'd', 'c', 'b', 'a']
car.sort();print(car)
['bmw', 'ford', 'tesla']
y=0
the=dict.frfomkeys(car,y)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    the=dict.frfomkeys(car,y)
AttributeError: type object 'dict' has no attribute 'frfomkeys'. Did you mean: 'fromkeys'?
the=dict.fromkeys(car,y)
print(the)
{'bmw': 0, 'ford': 0, 'tesla': 0}
x= car.setdefault("model","hyundai")
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    x= car.setdefault("model","hyundai")
>>> AttributeError: 'list' object has no attribute 'setdefault'
... car={
>>>     "brand": "h"}
>>> x=car.setdefault("brand","gg")
print(x)
>>> h
>>> car.update({"brand":"thasa"})
print(car)
>>> {'brand': 'thasa'}
x=car.value();print(car)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    x=car.value();print(car)
>>> AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
>>> x=car.values()
print(x)
>>> dict_values(['thasa'])
>>> n=(1,2,3,4,5)
>>> x= n.index(5)
print(x)
>>> 4
z=a.symmetric_difference(b)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    z=a.symmetric_difference(b)
>>> AttributeError: 'list' object has no attribute 'symmetric_difference'
>>> o=(2,8,9)
z=n.symmetric_difference(o);print(z)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    z=n.symmetric_difference(o);print(z)
>>> AttributeError: 'tuple' object has no attribute 'symmetric_difference'
>>> c=["a","b"];d=["e","f"]
f=c.symmetric_difference(d)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    f=c.symmetric_difference(d)
