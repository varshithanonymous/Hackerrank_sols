class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # 32-bit integer limits
        result = 0
        sign = -1 if x < 0 else 1  # Handle negative numbers
        x = abs(x)

        while x:
            digit = x % 10
            x //= 10

            # Check for overflow before updating result
            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result
