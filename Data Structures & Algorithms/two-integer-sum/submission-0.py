class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #okay we have to efficiently generate every sum combo and record the indexs in a list

        indexes = []

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    indexes.append(i)
                    indexes.append(j)

        return indexes
        