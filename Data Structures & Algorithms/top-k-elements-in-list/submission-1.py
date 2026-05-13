import collections 


class Solution:


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #idea: map num occurences to each unique number
        # sort the list in terms of most frequent to least frequent
        # then loop through k adding each most frequent to list

        frequent = []
        nums.sort(reverse = True)
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        listo = sorted(counts.items(), key = lambda item:item[1],reverse = True)

        for i in range(k):
            frequent.append(listo[i][0])

        return frequent
        