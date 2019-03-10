###### This problem was asked by:
<br>

![Palantir](https://seeklogo.net/wp-content/uploads/2015/09/palantir-logo-vector-download.jpg)

Write an algorithm to _justify_ text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully _justified_.

More specifically, you should have __as many words as possible in each line__. There should be at least one space between each word. Pad _extra spaces_ when necessary so that each line has exactly _length k_. Spaces should be distributed _as equally as possible_, with the extra spaces, if any, distributed _starting from the left_.

If you can only fit one word on a line, then you should pad the _right-hand_ side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words `["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]` and `k = 16`, you should return the following:
```python
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
```
