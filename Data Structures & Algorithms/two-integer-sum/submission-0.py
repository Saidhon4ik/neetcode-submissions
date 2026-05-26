class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,num in enumerate(nums):
            seen = target - num
            if seen in h:
                return [h[seen],i]
            else:
                h[num] = i
        return None