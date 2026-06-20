import string

class Solution:

    def is_alpha_numeric(self, c: str):

        alpha_lower_start = ord('a')
        alpha_lower_end = ord('z')

        alpha_upper_start = ord('A')
        alpha_upper_end = ord('Z')

        num_start = ord('0')
        num_end = ord('9')

        c_ord = ord(c)

        if (c_ord >= alpha_lower_start and c_ord <= alpha_lower_end or 
            c_ord >= alpha_upper_start and c_ord <= alpha_upper_end or 
            c_ord >= num_start and c_ord <= num_end):
            return True
        
        return False

    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) - 1

        while start < end:

            if not self.is_alpha_numeric(s[start]):
                start += 1
            elif not self.is_alpha_numeric(s[end]):
                end -= 1
            elif  s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        
        return True