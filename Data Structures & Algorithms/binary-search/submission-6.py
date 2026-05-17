class Solution:
    def search(self, nums: List[int], target: int) -> int:

        mini = 0
        maxi = len(nums)-1

        if(len(nums) == 1):
            if(nums[0] == target):
                return 0
            else:
                return -1
        
        while(mini <= maxi):
            midi = int((mini+maxi) /2)

            if(nums[midi] > target):
                maxi = midi - 1

            elif(nums[midi] < target):
                mini = midi + 1

            else:
                return midi

        return -1
        