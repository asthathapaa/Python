Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fun(**kid):
...     print("His last name is "+ kid["lname"])
... fun(fname= "Tobias",lname="ferne")
SyntaxError: invalid syntax
>>> 
>>> def fun(**kid):
...     print("His last name is "+ kid["lname"])
... 
>>> fun(fname= "Tobias",lname="ferne")
... 
His last name is ferne
>>> def fun(country= "NEPAL")
SyntaxError: expected ':'
>>> def fun(country= "NEPAL"):
...     print("My nationality is "+country)
... 
...     
>>> fun("Sydney")
My nationality is Sydney
>>> fun("Nepal")
My nationality is Nepal
>>> 
>>> def fun(food):
...     for x in food:
...         print(x)
... 
...         
>>> fruits=["ap","ba","gr"]
>>> fun(fruits)
ap
ba
gr
