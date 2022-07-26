# Apuntes de Python

## Python tips

https://codechalleng.es/tips/get-annotations
```python
Get annotations

You can get the type annotations of a function via its __annotations__ attribute:

>>> def hello(name:str) -> str:
...     return f"hola {name}"
... 
>>> 
>>> hello.__annotations__
{'name': <class 'str'>, 'return': <class 'str'>}
```
https://codechalleng.es/tips/dataclasses-and-order
```python
 Dataclasses and order

dataclasses are not orderable by default, 
unless you pass in order=True 
when constructing them:

>>> from dataclasses import dataclass
>>> @dataclass
... class Bite:
...     number: int
...     title: str
...     level: int = 0
... 
>>> bites = [
...     Bite(11, "uno", 1),
...     Bite(21, "query", 2),
...     Bite(31, "tres", 3),
... ]
>>> sorted(bites)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Bite' and 'Bite'
>>> @dataclass(order=True)
... class Bite:
...     number: int
...     title: str
...     level: int = 0
>>> bites2 = [Bite(1, "uno", 1), Bite(2, "dos", 2), Bite(3, "tres", 3)]
>>> sorted(bites2)
[Bite(number=1, title='uno', level=1), Bite(number=2, title='dos', level=2), Bite(number=3, title='tres', level=3)]
```