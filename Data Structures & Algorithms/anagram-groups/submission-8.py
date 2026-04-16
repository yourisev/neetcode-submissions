class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupings = {}
        for st in strs:
            tmp = [0] * 26
            for c in st:
                tmp[ord(c) - ord('a')]+=1
            key_ = tuple(tmp)
            if key_ in groupings:
                groupings[key_].append(st)
            else:
                groupings[key_] = [st]
        
        result = []

        for val in groupings.values():
            result.append(val)
        
        return result
        