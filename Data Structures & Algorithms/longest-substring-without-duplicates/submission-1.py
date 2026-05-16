class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if(len(s) == 0):
            return 0
        subo = 1

        for left in range(len(s)):
            right =left +1

            while(right != len(s) and s[right] not in s[left:right] and s[left]!= s[right]):
                right+=1
                if(len(s[left:right]) > subo):
                    print(s[left:right])
                    subo = len(s[left:right])

        return subo

            


            


        return len(subo)
            


        