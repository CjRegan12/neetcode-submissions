class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for num in nums:
            if num in frequent:
                frequent[num] += 1
            else:
                frequent[num] = 1

        ordered = sorted(frequent, key=frequent.get, reverse=True)
        return ordered[:k]


       
        
        