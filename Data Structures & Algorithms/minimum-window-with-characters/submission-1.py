class Solution:

    def checkContains(self,s, tFreq):

        contains = True

        for char in tFreq.keys():
            if(s.count(char) < tFreq[char]):
                contains = False

        return contains



    def minWindow(self, s: str, t: str) -> str:

        tFreq = {}

        for c in range(len(t)):
            tFreq[t[c]] = tFreq.get(t[c],0) + 1

        left = 0
        window_counts = {}
        satisfied = 0
        required = len(tFreq) 
        result = ""

        for right in range(len(s)):
            window_counts[s[right]] = window_counts.get(s[right], 0) + 1
            
            if s[right] in tFreq and window_counts[s[right]] == tFreq[s[right]]:
                satisfied += 1
            
            while satisfied == required:
                if not result or (right - left + 1) < len(result):
                    result = s[left:right+1]
                
                window_counts[s[left]] -= 1
                if s[left] in tFreq and window_counts[s[left]] < tFreq[s[left]]:
                    satisfied -= 1
                left += 1

        return result

        

        