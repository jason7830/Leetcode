"""
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for i , num in enumerate(nums):
            complement = target - num
            try :
                return [hashTable[complement],i]
            except:
                hashTable[nums[i]] = i
        print("Not Found!")


print(Solution().twoSum([2,7,6,8,10],13))
