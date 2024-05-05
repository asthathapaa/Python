Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="hello"
print(type(x))
<class 'str'>
y={"name":"john","age":36}
print(y)
{'name': 'john', 'age': 36}
print(type(y))
<class 'dict'>
x= range(6)
print(x)
range(0, 6)
print(type(x))
<class 'range'>

x={"apple","guava","cherry"}
print(type(x))
<class 'set'>
x= memoryview(bytes(5))

y= memoryview(bytes(5))

print(y)
<memory at 0x00000180E8003D00>
print(type(y))
<class 'memoryview'>
>>> #setting verification
>>> #to variable
>>> x= str("hello world")
>>> print(type(x))
<class 'str'>
>>> x= tuple(("apple","banana","cherry"))
>>> print(x)
('apple', 'banana', 'cherry')
>>> print(type(x))
<class 'tuple'>
>>> x= bool(5)
>>> y=bytes(5)
>>> print(x,y)
True b'\x00\x00\x00\x00\x00'
>>> print(type(x+y))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(type(x+y))
TypeError: unsupported operand type(s) for +: 'bool' and 'bytes'
>>> print(type(x))
<class 'bool'>
>>> print(type(y))
<class 'bytes'>
>>> x=1
>>> y=2.8
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> a= float(x)
>>> b= int(y)
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'int'>
>>> import random
>>> print(random.randrange(1,10))
2
>>> import random
>>> print(random.randrange(1,1000))
863
