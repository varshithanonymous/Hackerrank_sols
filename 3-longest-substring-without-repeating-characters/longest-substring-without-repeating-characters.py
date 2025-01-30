class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0  # Left boundary of the sliding window
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:  # If duplicate is found, shrink the window
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])  # Expand the window
            max_length = max(max_length, right - left + 1)

        return max_length
