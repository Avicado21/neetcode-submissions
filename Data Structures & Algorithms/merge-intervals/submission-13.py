class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort = sorted(intervals, key= lambda interval:interval[0])

        newList = [sort[0]]


        for i in range(1,len(sort)):
            val1 = newList[len(newList) -1]
            val2 = sort[i]

            if(val1[1] == val2[0] or val1[1] > val2[0]):
                newList[len(newList) -1] = [val1[0], max(val1[1],val2[1])]
            
            else:
                newList.append(val2)
        
        return newList



        