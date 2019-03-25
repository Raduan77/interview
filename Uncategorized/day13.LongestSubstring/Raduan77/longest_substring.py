def longest_substring(string, k):
    if k == 0:
        return 0
    counter = 0
    max = 0
    first_index = 0
    storage = {}
    for i in range(len(string)):
        if string[i] in storage.keys():
            storage[string[i]] += 1
        else:
            storage[string[i]] = 1
        counter += 1
        while len(storage.keys()) > k:
            storage[string[first_index]] -= 1
            if storage[string[first_index]] == 0:
                del storage[string[first_index]]
            counter -= 1
            first_index += 1
        if counter > max:
            max = counter
    return max


if __name__ == '__main__':
    assert longest_substring('abcba', 2) == 3
    assert longest_substring('aaaaa', 3) == 5
    assert longest_substring('fajfaksdfahifhjdsaklfjafjlkafjkdsf', 0) == 0
    assert longest_substring('abbbbbcbbbbzddda', 2) == 10
    assert longest_substring('', 2) == 0
    print('All tests has passed!')
