class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        solution = []
        front = 0
        back = len(numbers) - 1

        while front < back:
            temp = numbers[front] + numbers[back]

            if temp == target:
                solution.append(front + 1)
                solution.append(back + 1)
                return solution
            
            if temp > target:
                back -= 1
                continue

            if temp < target:
                front += 1
                continue