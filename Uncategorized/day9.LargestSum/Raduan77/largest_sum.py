def largest_sum(arr):
    if len(arr) == 1:
        return 0
    prev, cur = 0, 0
    for item in arr:
        if item+prev > cur:
            cur, prev = item+prev, cur
        else:
            cur, prev = cur, cur
    return cur


if __name__ == '__main__':
    assert largest_sum([2, 4, 6, 2, 5]) == 13
    assert largest_sum([5, 1, 1, 5]) == 10
    assert largest_sum([]) == 0
    assert largest_sum([1]) == 0
    print('All tests has passed')
