# coding: utf-8
'''
[unfinished!!!]
Implement atoi to convert a string to an integer.
'''
import ctypes

class Solution(object):
    '''
    solution
    '''
    def int32(self, x):
        '''
        :type x: int
        '''
        if x > 0xFFFFFFFF:
            raise OverflowError
        if x > 0x7FFFFFFF:
            x = int(0x100000000 - x)
            if x < 2147483648:
                return -x
            else:
                return -2147483648
        return x

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbol = ['+', '-']
        str = str.strip()
        end_index = 0
        for (index, item) in enumerate(str):
            if item in symbol:
                continue
            if item not in dig:
                end_index = index
                break
            else:
                end_index = index + 1
        str = str[:end_index]
        try:
            out = int(str)
            return ctypes.c_uint32(out).value
        except:
            return 0


a = Solution()
print(a.myAtoi('-0012a42'))
print(a.myAtoi(''))
print(a.myAtoi('a'))
print(a.myAtoi('1'))
print(a.myAtoi('+1'))
print(a.myAtoi('-_1'))
print(a.myAtoi('2147483648'))  # 2147483647
