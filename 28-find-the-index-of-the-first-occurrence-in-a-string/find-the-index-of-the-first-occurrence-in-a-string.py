class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Using a manual implementation for finding the first occurrence
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0  # Edge case: empty needle
        
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1
