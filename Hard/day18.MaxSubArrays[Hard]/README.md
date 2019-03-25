###### This problem was asked by
<br>

![Google](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png)

Given an array of integers and a number _k_, where `1 <= k <= length of the array`, compute the maximum values of each subarray of length _k_.

For example, given `array = [10, 5, 2, 7, 8, 7]` and `k = 3`, we should get: `[10, 7, 8, 8]`, since:

- `10 = max(10, 5, 2)`
- `7 = max(5, 2, 7)`
- `8 = max(2, 7, 8)`
- `8 = max(7, 8, 7)` <br>
Do this in `O(n)` time and `O(k)` space. You can modify the input array __in-place__ and you do not need to store the results. You can simply print them out as you compute them.
