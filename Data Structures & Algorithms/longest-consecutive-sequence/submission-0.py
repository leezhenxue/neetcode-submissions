class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_length = 0
        longest_start = 0
        current = 0
        length = 0

        for num in num_set:
            if num-1 not in num_set:
                current = num
                length = 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                if length > longest_length:
                    longest_length = length

        return longest_length