class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        if(len(nums) == 0):
            return 0

        if(len(nums) == 1):
            return 1

        runningtotal = 0

        val = nums[0]

        total = 0

        for i in range(1,len(nums)):

            if(nums[i] == val + 1):
                total +=1
                val = nums[i]
            
            elif(nums[i] == val):
                val = nums[i]
            else:
                val = nums[i]
                total = 0

            if(total + 1  >runningtotal):
                runningtotal = total +1

        return runningtotal

        