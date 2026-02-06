class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        x = 0
        y = 0
        for i in nums1:
            if i in nums2:
                x += 1
        for i in nums2:
            if i in nums1:
                y += 1
        return [x,y]