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
