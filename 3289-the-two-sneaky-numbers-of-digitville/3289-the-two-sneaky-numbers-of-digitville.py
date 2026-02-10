class Solution(object):
    def getSneakyNumbers(self, nums):
        additional_numbers = []
        set_nums = []
        for i in nums:
            if i not in set_nums:
                set_nums.append(i)
            else:
                additional_numbers.append(i)
        return additional_numbers
