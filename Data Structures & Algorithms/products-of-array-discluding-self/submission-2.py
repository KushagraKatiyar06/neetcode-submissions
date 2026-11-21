class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mul_left = 1
        mul_right = 1
        Left = [0] * n
        Right = [0] * n

        for i in range(n):
            Left[i] = mul_left
            mul_left *= nums[i]

        for j in range(n - 1, -1, -1):
            Right[j] = mul_right
            mul_right *= nums[j]

        result = []

        for k in range(n):
            result.append(Left[k] * Right[k])

        return result


