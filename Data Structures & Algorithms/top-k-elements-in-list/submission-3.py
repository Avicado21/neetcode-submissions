class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dicto = {}

        for i in range(len(nums)):
            if nums[i] not in dicto:
                dicto[nums[i]] = 1
            else:
                dicto[nums[i]] += 1

        # now I just have the get the values in sorted order for the given k amount

        sortedict = dict(sorted(dicto.items(), key=lambda item: item[1], reverse=True))
        
        listo = list(sortedict.keys())

        i= 0
        liste = []
        while(i < k):
            liste.append(listo[i])
            i+=1

        return liste

        