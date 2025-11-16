class Solution(object):
    def intersection(self, nums1, nums2):
        a=set(nums1)
        b=set(nums2)
        x=[]
        for i in a:
            if i in b:
                x.append(i)
            else:
                continue
        return x
        