###### This problem was asked by
<br>

![Google](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png)

Suppose we represent our file system by a string in the following manner:

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:
```
dir
    subdir1
    subdir2
        file.ext
```
The directory _dir_ contains an empty sub-directory _subdir1_ and a sub-directory _subdir2_ containing a file _file.ext_.

The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` represents:
```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```
The directory _dir_ contains two sub-directories _subdir1_ and _subdir2_. _subdir1_ contains a file _file1.ext_ and an empty second-level sub-directory _subsubdir1_. _subdir2_ contains a second-level sub-directory _subsubdir2_ containing a file _file2.ext_.

We are interested in finding the __longest (number of characters)__ absolute path to a file within our file system. For example, in the second example above, the longest absolute path is `"dir/subdir2/subsubdir2/file2.ext"`, and its length is __32__ (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
