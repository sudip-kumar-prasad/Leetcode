class Solution(object):
    def rearrangeArray(self, nums):
        pos_nums = []
        neg_nums = []
        for i in nums:
            if i>0:
                pos_nums.append(i)
            else:
                neg_nums.append(i)
        ans = []
        for i in range(len(pos_nums)):
            ans.append(pos_nums[i])
            ans.append(neg_nums[i])
        return ans


        