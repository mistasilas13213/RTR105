Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: ")
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 10]

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    input("Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: ")
  File "<string>", line 1
    10]
      ^
SyntaxError: unexpected EOF while parsing
>>> 10
10
>>> input("Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: ")
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainiigais = input("Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: ")
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 10
>>> vars()
{'mans_mainiigais': 10, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainiigais
10
>>> >>> mans_mainiigais = input("Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: ")

SyntaxError: invalid syntax
>>> mans_mainiigais = input("Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: ")
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 20
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainiigais)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 5
>>> vars()
{'mans_mainiigais': 5, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 8
>>> vars()
{'mans_mainiigais': 8, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> vars()
{'mans_mainiigais': 8, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 89
mans_mainiigais = 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 156
mans_mainiigais =  156
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 144
mans_mainiigais =  144
vai tu esi ievadījis skaitli: 144
vēl atmiņā ir arī mainīgais x = 20736

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 8, in <module>
    print(y)
NameError: name 'y' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 12
mans_mainiigais =  12
vai tu esi ievadījis skaitli: 12
vēl atmiņā ir arī mainīgais x = 144

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 8, in <module>
    print(y)
NameError: name 'y' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 12
mans_mainiigais =  12
vai tu esi ievadījis skaitli: 12
vēl atmiņā ir arī mainīgais x = 144
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 8.4683
mans_mainiigais =      8.468
vai tu esi ievadījis skaitli:     8.4683
vēl atmiņā ir arī mainīgais x =      71.7121049
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: 2547
mans_mainiigais =   2547.000
vai tu esi ievadījis skaitli:  2547.0000
vēl atmiņā ir arī mainīgais x = 6487209.0000000
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: aaaaa

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 2, in <module>
    x = mans_mainiigais * mans_mainiigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: aaaaaaaaa
mans_mainiigais = aaaaaaaaa
vai tu esi ievadījis skaitli: aaaaaaaaa

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 8, in <module>
    print("vēl atmiņā ir arī mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: aaaaaa\
mans_mainiigais = aaaaaa\
vai tu esi ievadījis skaitli: aaaaaa\

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 8, in <module>
    print("vēl atmiņā ir arī mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotājs, lūdzu ievadīt vienu skaitli: aaaaaa
mans_mainiigais = aaaaaa
vai tu esi ievadījis skaitli: aaaaaa

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 8, in <module>
    print("vēl atmiņā ir arī mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 

