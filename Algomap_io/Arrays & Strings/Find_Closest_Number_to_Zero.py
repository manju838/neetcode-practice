"""
# Method1:
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0] # Given nums has atleast 1 element

        for x in nums:
            if(abs(x) < abs(closest)):
                closest = x
        
        if (closest < 0 and abs(closest) in nums):
            return abs(closest)
        else:
            return closest
        
        # Time Complexity: O(2n) = O(n)
        # Space Complexity: O(1) only a single variable used (closest)
"""

# Method2:
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = min(abs(x) for x in nums)
        return ans if ans in nums else -ans
        