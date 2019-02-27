## This problem was asked by:
<br>
![Jane Street](https://www.janestreet.com/assets/logo_horizontal.png)

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns __3__, and `cdr(cons(3, 4))` returns __4__.

Given this implementation of cons:
```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement car and cdr.
###### Check-out `tests/` directory, and add any missed corner-cases
