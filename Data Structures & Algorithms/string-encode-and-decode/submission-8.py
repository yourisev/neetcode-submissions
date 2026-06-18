class Solution:

    def encode(self, strs: List[str]) -> str:

        concatenated_result = ""

        for str_ in strs:
            meta_data = str(len(str_))
            encoded_block = meta_data + "#" + str_
            concatenated_result += encoded_block
        
        return concatenated_result

    def get_meta_data(self, str_:str, pos: int):
        len_str = len(str_)
        len_block = ""
        while pos < len_str and str_[pos] != '#':
            len_block += str(str_[pos])
            pos += 1
        
        return [pos + 1, int(len_block)]

    def decode(self, s: str) -> List[str]:

        decoded_result = []
        i = 0

        while i < len(s):
            meta_data = self.get_meta_data(s,i)
            block = s[meta_data[0] : meta_data[0] + meta_data[1]]
            decoded_result.append(block)
            i = meta_data[0] + meta_data[1]
        
        return decoded_result