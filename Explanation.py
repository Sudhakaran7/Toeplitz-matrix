A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an N x N matrix, return True if and only if the matrix is Toeplitz.

Input Description:
First Line contains, N the size of the matrix.
Second line contains, N elements of the matrix in a single line.

Output Description:
Print True of Flase.

Sample Input:
4
1 2 2 1

Sample Output:
True

Explanation:
The given matrix is,
1 2
2 1, since the diagonal matrix are same the output is True.

Sample Input:
3
2 3 4 7 2 4 8 4 2

Sample Output:
False

Sample Input:
4
1 2 3 4 5 1 2 3 6 7 1 9 10 23 14 1

Sample Output:
False

Sample Input:
2
0 1 0 1

Sample Output:
False

Sample Input:
3
1 1 1 1 1 1 1 1 1

Sample Output:
True

Sample Input:
3
99 1 1 100 100 100 1 1 1

Sample Output:
False
