def helper(string, i, storage):
    if len(string) - i <= 0:
        return 1
    if int(string[i]) == 0:
        return 0
    if storage[i]:
        return storage[i]
    result = helper(string, i+1, storage)
    if len(string) - i >= 2 and (9 < int(string[i:i+2]) < 27):
        result += helper(string, i+2, storage)
    storage[i] = result
    return result


def count(string):
    storage = [None]*(len(string))
    return helper(string, 0, storage)


if __name__ == '__main__':
    assert count('111') == 3
    assert count('01') == 0
    assert count('1308') == 0
    assert count('11111') == 8
    print('All tests has passed!')
