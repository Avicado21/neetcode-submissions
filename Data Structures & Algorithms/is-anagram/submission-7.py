class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)

        tlist.sort()
        slist.sort()

        return (slist == tlist)
        