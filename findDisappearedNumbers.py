class Solution:
     def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        found = {}
        for num in nums:
            found[num] = True
        
        result = []
        for i in range(1, len(nums) + 1):
            if i not in found:
                result.append(i)
        
        return result
