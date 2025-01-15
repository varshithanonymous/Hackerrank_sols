class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        set_bits_count = bin(num2).count('1')  # Count the number of set bits in num2
        result = 0
        
        # Set the bits from the most significant bit of num1
        for i in range(31, -1, -1):  # Assume 32-bit integers
            if set_bits_count > 0 and (num1 & (1 << i)) != 0:
                result |= (1 << i)
                set_bits_count -= 1
        
        # If there are still bits left to set, use the smallest unset bits (from the least significant)
        for i in range(32):
            if set_bits_count > 0 and (result & (1 << i)) == 0:
                result |= (1 << i)
                set_bits_count -= 1
        
        return result
