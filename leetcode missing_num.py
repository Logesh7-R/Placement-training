'''
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        # j=1
        # for i in range(0,len(nums)):
        #     if nums[i] > 0:
        #         if(nums[i] == nums[i-1] and i-1 != -1):
        #             continue
                    
        #         if j==nums[i]:
        #             j+=1
        #         else:
        #             return j

        # return j
        nums=set(nums)
        ans=1

        while ans in nums:
            ans+=1
        return ans

#should write code for getting inputs
