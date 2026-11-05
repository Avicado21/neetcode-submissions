class Solution:
    def climbStairs(self, n: int) -> int:

        ways = []

        for i in range(n+2):
            if(i == 0):
                ways.append(0)
            elif(i == 1):
                ways.append(1)
            else:
                ways.append(ways[i-1] + ways[i-2])

        return(ways[n+1])


        