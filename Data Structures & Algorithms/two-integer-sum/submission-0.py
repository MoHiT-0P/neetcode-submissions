class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for ind,n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[diff], ind]
            d[n] = ind