class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        Anagram = True

        sList = list(s)
        tList = list(t)

        sList.sort()

        tList.sort()

        print(sList)
        print(tList)

        if(len(s) != len(t)):
            Anagram = False
        else:
            for i in range(len(sList)):
                if(sList[i] != tList[i]):
                    Anagram = False

        return Anagram

        