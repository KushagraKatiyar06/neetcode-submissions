class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        solution = []

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum == target:
                solution.append(l + 1)
                solution.append(r + 1)
                return solution
            if currentSum < target:
                l += 1
            if currentSum > target:
                r -= 1
    