class Solution(object):
    def distributeCandies(self, candyType):
        unique_candies = set(candyType)
        max_candies = len(candyType) // 2
        return min(len(unique_candies), max_candies)
