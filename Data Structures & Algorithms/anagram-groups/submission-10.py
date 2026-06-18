class Solution:
    def get_key(self, str_:str):
        vocab = [0] * 26

        for c in str_:
            vocab[ord(c) - ord('a')] += 1
        
        return tuple(vocab)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_grouped = []
        anagram_map = {}

        for str_ in strs:
            anagram_key = self.get_key(str_)
            if anagram_key not in anagram_map:
                anagram_map[anagram_key] = []
            anagram_map[anagram_key].append(str_)
        
        for group in anagram_map.values():
            anagrams_grouped.append(group)
        
        return anagrams_grouped