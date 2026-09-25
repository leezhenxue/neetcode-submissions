class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for word in strs:
            encoded_list.append(str(len(word)) + "#" + word)
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        index = 0
        while index < len(s):
            length_str = ""
            while s[index] != "#":
                length_str += s[index]
                index += 1
            index += 1
            length = int(length_str)
            decoded_strs.append(s[index:(index+length)])
            index += length


        return decoded_strs

