class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        current_sum = numbers[left] + numbers[right]

        while left < right and current_sum != target:
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            current_sum = numbers[left] + numbers[right]
        return [left + 1, right + 1]