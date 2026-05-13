class Solution:

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #okay so we take all the words break them up into lists of letters per word
        #then compare each word's breakdown to all the others
        #then add those matches to a new list and store that onto the returned list
        #if no matches then we just add the initial
        #we should also remove all the matched words for brevity

        group = []

        usedWords = []

        for i in range(len(strs)):

            if(strs[i] not in usedWords):
                listo = []
                listo.append(strs[i])
                for j in range(i+1,len(strs)):
                    l1 = list(strs[i])
                    l2 = list(strs[j])
                    l1.sort()
                    l2.sort()
                    if(l1 == l2):
                        listo.append(strs[j])
                group.append(listo)

            for g in group:
                for w in g:
                    if(w not in usedWords):
                        usedWords.append(w)

        return group


        
        