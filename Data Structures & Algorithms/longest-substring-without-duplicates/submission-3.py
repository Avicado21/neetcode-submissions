class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        leng = 0

        left = 0

        seen = set()

        for right in range(len(s)):

            while(s[right] in seen):
                seen.remove(s[left])
                left+=1

            seen.add(s[right])

            if(len(s[left:right+1]) > leng):
                leng = len(s[left:right+1])

        return leng
            


        