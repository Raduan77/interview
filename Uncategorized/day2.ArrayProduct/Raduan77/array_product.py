'''
Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers
in the original array except the one at i.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be
`[120, 60, 40, 30, 24]`.
If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

Follow-up: what if you __can't__ use `division`?
'''
import os


def division(dividend, divisor):
    if divisor == 0:
        raise ArithmeticError
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    counter = 0
    while dividend >= divisor:
        counter += 1
        dividend -= divisor
    return sign * counter


def find_product_array(array):
    null_counter = 0
    null_index = -1
    product = 1
    for index, item in enumerate(array):
        if item == 0:
            null_counter += 1
            null_index = index
            if null_counter > 1:
                return [0] * len(array)
            continue
        product *= item
    if null_counter > 0:
        return [0 if i != null_index else product for i in range(len(array))]
    return [division(product, item) for item in array]


if __name__ == '__main__':
    os.chdir('..')
    path = os.path.abspath(os.getcwd()) + "/tests/"
    for i in range(4):
        with open(path+f"test{i+1}.txt", 'r') as f:
            _ = f.readline().rstrip()
            array = list(map(int, f.readline().rstrip().split()))
            result_array = list(map(int, f.readline().rstrip().split()))
            if find_product_array(array) == result_array:
                print(f"Test {i+1} passed!")
            else:
                print(f"Test {i+1} failed!")
