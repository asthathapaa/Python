Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 2
while a < 4:
    print(a)
    a = a +1

    
2
3
i=1
while i<10:
    print(i)
    i++
    
SyntaxError: invalid syntax
while i<10:
    print(i)
    i= i+1

    
1
2
3
4
5
6
7
8
9
while i<11:
    print(i)
    i= i+1

    
10
row = 5
for i in range(1 ,row+1 ,1)
SyntaxError: expected ':'
>>> for i in range(1 ,row+1 ,1):
...     for j in range(1 ,col,1):
...         print(i)
... 
...         
Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    for j in range(1 ,col,1):
NameError: name 'col' is not defined
>>> for i in range(1 ,row+1 ,1):
...     for j in range(1 ,i+1):
...         print(j, end=' ')
...     print(" ")
... 
...     
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5  
>>> for i in range(1 ,row+1 ):
...     for j in range(1 ,i+1):
...         print(j, end=' ')
...     print(" ")
... 
...     
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5  
>>> range(0,10)
range(0, 10)
>>>  i = 1
...  
SyntaxError: unexpected indent
>>> i = 1;
>>> range(i,10)
range(1, 10)
>>> input('enter a number :')
enter a number :
''
>>> input('enter a number :');
enter a number :
''
