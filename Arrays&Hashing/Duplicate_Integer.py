"""
# Solution1: Hashset method
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Solution2: Hashtable method
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for a in nums:
            if(a in hash_table.keys()):
                return True
            else:
                hash_table[a] = 1
        return False
"""