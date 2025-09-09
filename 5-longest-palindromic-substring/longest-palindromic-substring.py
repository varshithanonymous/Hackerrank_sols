class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0

        def expandAroundCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length of palindrome

        for i in range(len(s)):
            len1 = expandAroundCenter(i, i)       # odd length
            len2 = expandAroundCenter(i, i + 1)   # even length
            max_len = max(len1, len2)
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end+1]
