class Solution:

    def encode(self, strs: List[str]) -> str:

        marker = "::"
        encoded_str = ""

        for s in strs:
            s_length = len(s) + 2
            encoded_str = encoded_str + (str(s_length) + marker) + s        
        return encoded_str


    def decode(self, s: str) -> List[str]:

        result = []
        marker = "::"
        size_s = len(s)
        i = 0

        while i < size_s:

            tmp = ""
            j = i

            while j < size_s and s[j] != ':':
                tmp = tmp + s[j]
                j += 1
            
            sb_str_size = int(tmp) - 2
            result.append(s[ j + 2 : j + 2 + sb_str_size])
            i = j + sb_str_size + 2

        
        return result



