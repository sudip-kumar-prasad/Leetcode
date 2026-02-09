class Solution(object):
    def pivotArray(self, nums, pivot):
        x = []
        for i in nums:
            if pivot == i:
                x.append(i)
        less_pivot = []
        more_pivot = []
        for i in range(len(nums)):
            if nums[i]<pivot:
                less_pivot.append(nums[i])
            elif nums[i]>pivot:
                more_pivot.append(nums[i])
        return less_pivot + x + more_pivot
        