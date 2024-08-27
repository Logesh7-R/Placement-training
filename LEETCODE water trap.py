'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        # c=len(height)*max(height) - sum(height)
        # maxi=0
        # for i in range(0,len(height)):
        #     if(max(height) == height[i]):
        #         break
        #     if(maxi<height[i]):
        #         maxi = height[i]
                
        #     c-=(max(height)-maxi)
        # maxi = 0      
        # for i in range(len(height)-1,-1,-1):
        #     if(max(height) == height[i]):
        #         break
        #     if(maxi<height[i]):
        #         maxi = height[i]
        #     c-=(max(height)-maxi)
        # return c
        l=0
        c=0
        r=len(height)-1
        l_max=height[l]
        r_max=height[r]
        while l<r:
            if l_max<r_max:
                l+=1
                l_max=max(l_max,height[l])
                c+=(l_max-height[l])
            else:
                r-=1
                r_max=max(r_max,height[r])
                c+=(r_max-height[r])
        return c
# USE TWO POINTER CONCEPT
# only logic  
