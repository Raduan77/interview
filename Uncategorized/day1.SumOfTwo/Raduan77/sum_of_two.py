import os
"""
This problem was recently asked by Google.

Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def has_sum(array, value):
    storage = {}
    for item in array:
        if (value - item) in storage:
            return True
        storage[item] = ""
    return False


if __name__ == "__main__":
    assert has_sum([10], 10) == False
    assert has_sum([10, 15, 3, 7], 17) == True
    # print("All tests passed!")
    os.chdir('..')
    path = os.path.abspath(os.getcwd()) + "/tests/"
    for i in range(4):
        with open(path+f"test{i+1}.txt", 'r') as f:
            _ = int(f.readline().rstrip())
            array = list(map(int, f.readline().rstrip().split()))
            result = int(f.readline().rstrip())
            awaited_result = f.readline().rstrip()
            if(str(has_sum(array, result)).lower() == awaited_result):
                print(f"Test {i+1} passed!")
            else:
                print(f"Test {i+1} failed!")
