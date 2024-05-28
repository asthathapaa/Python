Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
i=1
while(i<6):
    print(i)
    if i==3:
        break;
    i+=1

    
1
2
3

i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

    
1
2
4
5
6
while i<6:
    print(i)
    i +=1
else:
    print("no longer less than 6")

    
no longer less than 6

fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)

    
apple
banana
cherry
for x in "banana":
    print(x)

    
b
a
n
a
n
a
for y in
SyntaxError: invalid syntax
for y in "cherry":
    print(y)

    
c
h
e
r
r
y
for x in fruits:
    print(x)
    if x == "banana":
        break

    
apple
banana
for x in fruits:
    
    if x == "banana":
        continue
    print(x)

    
apple
cherry
for x in range(6):
    print(x)

    
0
1
2
3
4
5
for x in range(-2):
    print(x)

    
for x in range(2,6)
SyntaxError: expected ':'
for x in range(2,6):
    print(x)

    
2
3
4
5
for x in range(8):
    if x ==3:
        break
    else:
        print("sakyo")

        
sakyo
sakyo
sakyo
>>> for x in range(8):
...     if x ==3:
...         break
...     print(x)
...     else:
...         print("sakyo")
...         
SyntaxError: invalid syntax
>>> for x in range(8):
...     if x ==3:
...         break
...         print(x)
...     else:
...         print("sakyo")
... 
...         
sakyo
sakyo
sakyo
>>>  for x in range(8):
...         if x ==3:
...             break
...             print(x)
...         else:
...             print(x++)
...             
SyntaxError: unexpected indent
>>> for x in range(8):
...        if x ==3:
...            break
...            print(x)
...        else:
...            x=x+1
... 
...            
>>> for x in [0,1,2]:
...     pass
... 
