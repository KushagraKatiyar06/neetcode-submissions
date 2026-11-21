class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right = len(numbers) - 1
        left = 0
        result = []

        while right > left:
            if numbers[right] + numbers[left] > target:
                right -= 1

            elif numbers[left] + numbers[right] < target:
                left += 1

            elif numbers[left] + numbers[right] == target and right != left:
                result.append(left + 1)
                result.append(right + 1)
                return result

        return result
        

        