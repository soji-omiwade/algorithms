'''
start: 1:42?
end: 

left and right pointers
come from both ends until sum of left and right equals target
if the sum isn't target. then if it is more than target decrement right. otherwise increment left
T: O(n) S: O(1)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            twosum = numbers[left] + numbers[right]     #17
            if twosum == target:
                return [1 + left, 1 + right]
            elif twosum < target:
                left += 1
            else:
                right -= 1
        raise ValueError("numbers has no two sum")