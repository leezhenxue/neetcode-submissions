class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in seen.items():
            bucket[count].append(num)

        i = len(nums)
        ans = []
        while k > 0:
            if not bucket[i]:
                i -= 1
                continue
            for num in bucket[i]:
                ans.append(num)
                k -= 1
            i -=1
        
        return ans