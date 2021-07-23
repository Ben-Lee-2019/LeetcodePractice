'''
Descripttion: 
version: 
Author: liben
Date: 2021-05-13 15:44:41
LastEditors: liben
LastEditTime: 2021-05-13 15:47:54
'''
class Solution:
    def twoSum(self, nums, target: int):
        dic={}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [i,dic[target-nums[i]]]
         
            dic[nums[i]]=i       