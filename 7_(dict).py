Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
thisset={"apple","bannana"}
print(thisset)
{'apple', 'bannana'}
thiset={"ap","ba",ch,"True","False",o}
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    thiset={"ap","ba",ch,"True","False",o}
NameError: name 'ch' is not defined. Did you mean: 'chr'?
thiset={"ap","ba","ch","True","False",o}
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    thiset={"ap","ba","ch","True","False",o}
NameError: name 'o' is not defined
thiset={"ap","ba","ch","True","False",0}
print(thiset)
{'ap', 0, 'ch', 'ba', 'False', 'True'}

x=("apple","banana")
y= list(x)
y[1]= "kiwi"
x= tuple(y)
print(x)
('apple', 'kiwi')

y= list(x)
y.append("orng")
x= tuple(x)
print(x)
('apple', 'kiwi')
z=("org",)
x += y
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x += y
TypeError: can only concatenate tuple (not "list") to tuple
x+= z
print(x)
('apple', 'kiwi', 'org')

y= list(x)
y.remove("apple")
x= tuple(y)
print(x)
('kiwi', 'org')
del thisset
print(thisset)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(thisset)
NameError: name 'thisset' is not defined. Did you mean: 'thiset'?
fruits= {"apple","ba","ch"}
{grape,mango,app)= fruits
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
{grape,mango,app}= fruits
SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?
{grape,mango,app} == fruits
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    {grape,mango,app} == fruits
NameError: name 'grape' is not defined
{"grape","mango","app"} == fruits
False
{"grape","mango","app"} = fruits
SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?
fruits= ("apple","ba","ch")
("grape","mango","app") = fruits
SyntaxError: cannot assign to literal

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
apple
print(yellow)
banana
print(red)
cherry
fruits = ("apple", "banana", "cherry","ras")
(green, yellow, *red) = fruits
print(green)
apple
print(yellow)
banana
print(red)
['cherry', 'ras']
for x in fruits:
    print(x)

    
apple
banana
cherry
ras
for i in range(len(fruits)):
    print(fruits[i])

    
apple
banana
cherry
ras

myfav={
    "song" :{
        "name"= "wishywh",
        
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
myfav={
    "song" :{
        "name" : "wishywh",
        "yr" : 1990
        },
     "movie":{
         "name":"wonder",
         "yr":2017
         }
    "langu":{
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
myfav={
    "song" :{
        "name" : "wishywh",
        "yr" : 1990
        },
     "movie":{
         "name":"wonder",
         "yr":2017
         },
    "langu":{
        "name": "py",
        "yr":2024
        }
    }
print(myfav())
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print(myfav())
TypeError: 'dict' object is not callable
print(myfav)
{'song': {'name': 'wishywh', 'yr': 1990}, 'movie': {'name': 'wonder', 'yr': 2017}, 'langu': {'name': 'py', 'yr': 2024}}
myfav ={
    "song": song,
    "movie": movie,
    "langu":lg
    }
Traceback (most recent call last):
  File "<pyshell#77>", line 2, in <module>
    "song": song,
NameError: name 'song' is not defined
  "song" ={
        "name" : "wishywh",
        "yr" : 1990
        },
     "movie"={
         "name":"wonder",
         "yr":2017
         },
    "langu"={
        "name": "py",
        "yr":2024
        }
myfav ={
    "song": song,
    "movie": movie,
    "langu":lg
    }
SyntaxError: unexpected indent
}SyntaxError: unexpected indent
    
SyntaxError: unmatched '}'
"song" ={
      "name" : "wishywh",
      "yr" : 1990
      },
   "movie"={
       "name":"wonder",
       "yr":2017
       },
  "langu"={
      "name": "py",
      "yr":2024
      }
myfav ={
  "song": song,
  "movie": movie,
  "langu":langu
  }
    
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
song={
      "name" : "wishywh",
      "yr" : 1990
      },
movie={
       "name":"wonder",
       "yr":2017
       },
langu={
      "name": "py",
      "yr":2024
      }
myfav ={
  "song": song,
  "movie": movie,
  "langu":langu
  }
    
SyntaxError: multiple statements found while compiling a single statement
song={
      "name" : "wishywh",
      "yr" : 1990
      }
movie={
       "name":"wonder",
       "yr":2017
       }
langu={
      "name": "py",
      "yr":2024
      }
myfav ={
  "song": song,
  "movie": movie,
  "langu":langu
  }
    
SyntaxError: multiple statements found while compiling a single statement
song={
    "name" : "wishywh",
    "yr" : 1990
}
movie={
       "name":"wonder",
       "yr":2017
}
langu={
      "name": "py",
      "yr":2024
}
myfav ={
  "song": wishywh,
  "movie": movie,
  "langu":langu
}
    
SyntaxError: multiple statements found while compiling a single statement
song={
    "name" : "wishywh",
    "yr" : 1990
}
    
movie={
       "name":"wonder",
       "yr":2017
}
    
langu={
      "name": "py",
      "yr":2024
}
    
myfav ={
  "song": wishywh,
  "movie": wonder,
  "langu": py
}
    
SyntaxError: multiple statements found while compiling a single statement
song={
    "name" : "wishywh",
    "yr" : 1990
}
movie={
       "name":"wonder",
       "yr":2017
}
langu={
      "name": "py",
      "yr":2024
}
myfav ={
  "song": song,
  "movie": movie,
  "langu":langu
}
    
SyntaxError: multiple statements found while compiling a single statement
song={
    "name" : "wishywh",
    "yr" : 1990 ,
}
movie={
       "name":"wonder",
       "yr":2017 ,
}
langu={
      "name": "py",
      "yr":2024
}
myfav ={
  "song": song,
  "movie": movie,
  "langu":langu
}
    
SyntaxError: multiple statements found while compiling a single statement
song={
     "name": "emily",
     "year": 2002
     }
    
myfam={
    "song":song,
    }
    
print(myfam)
    
{'song': {'name': 'emily', 'year': 2002}}
print(myfav["song"]["name"])
    
wishywh
myfav={
    "song" :{
        "name" : "wishywh",
        "yr" : 1990
        },
     "movie":{
         "name":"wonder",
         "yr":2017
         },
    "langu":{
        "name": "py",
        "yr":2024
        }
    }
    
for x,obj in myfav.items():
    print(x)
    for y in obj:
    print(y+":",obj[y])
    
SyntaxError: expected an indented block after 'for' statement on line 3
for x,obj in myfav.items():
    print(x)

    
song
movie
langu
>>> for x,obj in myfav.items():
...     print(x)
... 
...     
song
movie
langu
>>> for x,obj in myfav.items():
...     print(x)
...     
...     for y in obj:
...     print(y+":",obj[y])
...     
SyntaxError: expected an indented block after 'for' statement on line 4
>>> for x,obj in myfav.items():
...     print(x)
... 
...     for y in obj:
...         print(y+":",obj[y])
... 
...     
song
name: wishywh
yr: 1990
movie
name: wonder
yr: 2017
langu
name: py
yr: 2024
>>> car= {
...     "barnd": "Ford",
...     "model": "mustang",
...     "year": 2000
...     }
...     
>>> x= car.copy()
...     
>>> print(x)
...     
{'barnd': 'Ford', 'model': 'mustang', 'year': 2000}
