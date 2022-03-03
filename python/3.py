'''
Descripttion: 
version: 
Author: liben
Date: 2022-01-25 15:50:03
LastEditors: liben
LastEditTime: 2022-01-25 15:54:05
'''
from json.tool import main


class Solution:
    def findRepeatNumber(self, nums):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return nums[i]
            else:
                dic[nums[i]] = 1

if __name__ == "__main__":
    nums = [1,2,3,4,5,1]
    s = Solution()
    print(s.findRepeatNumber(nums))
    
        