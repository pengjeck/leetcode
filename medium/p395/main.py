# coding: utf-8
'''
Given an array of integers A and let n to be its length.
Assume Bk to be an array obtained by rotating the array A k
positions clock-wise, we define a "rotation function" F on A as follow:
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
Calculate the maximum value of F(0), F(1), ..., F(n-1).
'''


class Solution(object):
    '''
    solution
    '''

    def rotate(self, in_list):
        '''
        rotate
        '''
        output = in_list[:-1]
        output.insert(0, in_list[-1])
        return output

    def multiplication(self, in_list):
        '''
        multiplication
        '''
        return [i * in_list[i] for i in range(len(in_list))]

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 1:
            return 0
        before = A
        result = []
        for _ in range(len(A)):
            before = self.rotate(before)
            out = self.multiplication(before)
            result.append(sum(out))

        return max(result)


solution = Solution()
# res = solution.maxRotateFunction([4, 3, 2, 6])
res = solution.maxRotateFunction([])
print(res)
