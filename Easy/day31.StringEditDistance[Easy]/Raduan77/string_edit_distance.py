def edit_distance(first_string, second_string):
    if (not first_string) and (not second_string):
        return 0
    storage = [[None for _ in range(len(first_string)+1)]
               for _ in range(len(second_string)+1)]
    for i in range(len(first_string)+1):
        storage[0][i] = i
    for j in range(len(second_string)+1):
        storage[j][0] = j
    for i in range(1, len(second_string)+1):
        for j in range(1, len(first_string)+1):
            insertion = storage[i][j-1]+1
            deletion = storage[i-1][j]+1
            match = storage[i-1][j-1]
            mismatch = match+1
            if first_string[j-1] == second_string[i-1]:
                storage[i][j] = min((insertion, deletion, match))
            else:
                storage[i][j] = min((insertion, deletion, mismatch))
    return storage[-1][-1]


if __name__ == '__main__':
    assert edit_distance('distance', 'editing') == 5
    assert edit_distance('abc', 'abc') == 0
    assert edit_distance('abc', 'axybc') == 2
    assert edit_distance('', '') == 0
    assert edit_distance('', 'abbc') == 4
    print('All tests has passed!')
