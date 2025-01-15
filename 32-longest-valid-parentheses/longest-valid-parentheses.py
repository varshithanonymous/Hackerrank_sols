class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize with -1 to handle edge cases
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push the index of '(' onto the stack
            else:
                stack.pop()  # Pop the last unmatched '('
                if not stack:
                    stack.append(i)  # Push the current index as a new base
                else:
                    max_length = max(max_length, i - stack[-1])  # Calculate the length of the valid substring
                    
        return max_length