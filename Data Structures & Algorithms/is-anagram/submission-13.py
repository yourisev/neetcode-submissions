class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        frequencies = [0 for _ in range(26)]

        for i in range(len(s)):
            frequencies[ord(s[i]) - ord('a')] += 1
            frequencies[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
            if frequencies[i] != 0:
                return False
        
        return True