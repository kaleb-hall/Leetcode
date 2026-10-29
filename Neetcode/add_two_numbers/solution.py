from leetcode_py import ListNode
import sys

class Solution:
    # Time: O(?)
    # Space: O(?)
    def add_two_numbers(self, nums: ListNode[int], target: int | None) -> ListNode[int] | None:
        # TODO: Implement add_two_numbers
        result = []
        for i in range(sys.getsizeof(nums)):
            for j in range(sys.getsizeof(nums)):
                if nums[i]+nums[j] == target:
                    result = []
                    break
        return result
