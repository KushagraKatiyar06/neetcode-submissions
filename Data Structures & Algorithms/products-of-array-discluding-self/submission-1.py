class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul = 1
        right_mul = 1

        n = len(nums)

        left = [0] * n
        right = [0] * n

        left[0] = 1
        right[n - 1] = 1

        i = 1
        j = len(nums) - 2

        while i < len(nums):
            
            left_mul *= nums[i - 1]
            right_mul *= nums[j + 1]

            left[i] = left_mul
            right[j] = right_mul


            i += 1
            j -= 1

        result = []
        k = 0
        while k < len(nums):
            result.append(left[k] * right[k])
            k += 1

        return result


