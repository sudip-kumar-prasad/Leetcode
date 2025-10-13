class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}  # key: (idx, curr_sum), value: number of ways

        def solve(idx, curr_sum):
            # Base case: all numbers have been used
            if idx == len(nums):
                return 1 if curr_sum == target else 0

            # Check memo
            if (idx, curr_sum) in memo:
                return memo[(idx, curr_sum)]

            # Take '+' sign
            take = solve(idx + 1, curr_sum + nums[idx])
            # Take '-' sign
            leave = solve(idx + 1, curr_sum - nums[idx])
            memo[(idx, curr_sum)] = take + leave
            return memo[(idx, curr_sum)]

        return solve(0, 0)
