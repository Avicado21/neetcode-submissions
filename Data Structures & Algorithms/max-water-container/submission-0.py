class Solution:
    def maxArea(self, heights: List[int]) -> int:

        p1 = 0

        p2 = len(heights) - 1

        wat = 0

        while(p1<p2):

            water = min(heights[p1],heights[p2]) * (p2-p1)

            if water > wat:
                wat = water

            if(heights[p1] > heights[p2]):
                p2 -= 1
            else:
                p1 +=1

        return wat


            
        