'''
I'm not 100% sure, that guys, that were asking this problem,
wanted exactly that implementation.
If you have better ideas - feel free to contribute
'''


def cons(a, b):
    def pair(f):
        return f((a, b))
    return pair(tuple)


def car(pair):
    return pair[0]


def cdr(pair):
    return pair[1]


if __name__ == '__main__':
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
    print("All tests has passed!")
