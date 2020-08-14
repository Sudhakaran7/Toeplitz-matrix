import numpy as np
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
val=Solution()
n=int(input())
R=n
C=n
nums=list(map(int,input().split()))
matrix=np.array(nums).reshape(R,C)
print(val.isToeplitzMatrix(matrix))
