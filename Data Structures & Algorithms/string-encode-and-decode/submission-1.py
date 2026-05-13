class Solution:

    def encode(self, strs: List[str]) -> str:
        bigstr = ""

        for str1 in strs:
            bigstr = bigstr+ "-" + str1 

        return bigstr

    def decode(self, s: str) -> List[str]:
        words = s.split("-")
        words.remove(words[0])
        return words
