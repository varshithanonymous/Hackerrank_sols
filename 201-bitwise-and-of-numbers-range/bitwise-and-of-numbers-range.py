class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shift = 0
        # Find the common prefix of left and right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        # Shift the result back to the original position
        return left << shift
