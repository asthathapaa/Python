Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def my_fun():
    prrint("hello")

    
def my_fun():
    prrint("hello")

    
def myfun():
    print("hello fun")
myfun()
SyntaxError: invalid syntax
def myfun():
    print("hello fun")

myfun()
hello fun

def myfun(fname):
...     print(fname+"Rexyr")
... 
...     
>>> myfun("AStga")
AStgaRexyr
>>> def myfun(fname):
...     print(fname+" Rexyr")
... 
...     
>>> myfun("lizzo")
lizzo Rexyr
>>> def myfun(fname, lname):
...     print(fname +" "+ lname)
... 
...     
>>> myfun("Astha","Thapa")
Astha Thapa
>>> def fun(Mtname, Location):
...     print(Mtname +" ,"+Location)
... 
...     
>>> fun("Mt.Annapurna","Sinwa")
Mt.Annapurna ,Sinwa
>>> def fun(Mtname, Location):
...     print("I love"+" "+Mtname +" ,"+"It lies at"+Location)
... 
...     
>>> fun("Mt.Annapurna","Ghorepani")
I love Mt.Annapurna ,It lies atGhorepani
>>> def my_fun(*kids):
...     print("The youngest child is" +kids[2])
... 
...     
>>> my_fun("Amin","Ashree","Aasmin")
The youngest child isAasmin
>>> def my_fun(*kids):
...     print("The youngest child is " +kids[2])
... 
...     
>>> my_fun("Amin","Ashree","Aasmin")
The youngest child is Aasmin
