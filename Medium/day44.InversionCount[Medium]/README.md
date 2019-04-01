###### This problem was asked by:
<br>

![Google](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png)

We can determine how _"out of order"_ an array A is by counting the number of _inversions_ it has. Two elements A[i] and A[j] form an _inversion_ `if A[i] > A[j] but i < j`. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than `O(N^2)` time.

You may assume each element in the array is _distinct_.

For example, a sorted list has *zero* inversions. The array `[2, 4, 1, 3, 5]` has three inversions: `(2, 1)`, `(4, 1)`, and `(4, 3)`. The array `[5, 4, 3, 2, 1]` has *ten* inversions: every distinct pair forms an inversion.
