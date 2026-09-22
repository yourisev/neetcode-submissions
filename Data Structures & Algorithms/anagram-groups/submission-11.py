from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def getKey(word:str):

            frequencies = [0 for _ in range(26)]

            for ch in word:
                frequencies[ord(ch) - ord('a')] += 1
            
            return str(frequencies)
        
        anagramsGroup = defaultdict(list)

        for word in strs:
            key_ = getKey(word)

            anagramsGroup[key_].append(word)
        
        return list(anagramsGroup.values())
        