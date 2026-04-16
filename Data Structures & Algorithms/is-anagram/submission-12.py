class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        frequencies = [0] * 26

        for i in range(len(s)):
            frequencies[ord(s[i]) - ord('a')]+=1
        
        for i in range(len(t)):
            if frequencies[ord(t[i]) - ord('a')] == 0:
                return False
            frequencies[ord(t[i]) - ord('a')]-=1
        
        return True




        