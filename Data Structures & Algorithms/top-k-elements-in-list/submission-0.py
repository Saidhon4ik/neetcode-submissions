class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
    
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        max_val = 0
        for val in count.values():
            if val > max_val:
                max_val = val
        
        answer = []
        for key, val in count.items():
            if val == max_val:
                answer.append(key)
        
        return answer