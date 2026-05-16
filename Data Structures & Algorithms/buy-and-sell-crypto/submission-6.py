class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for left in range(len(prices)):

            if(left + 1 != len(prices)):
                right = left +1
                
                if(prices[right] - prices[left]  > profit):
                    profit = prices[right] - prices[left]


                if(prices[right] > prices[left]):
                    while(right +1 != len(prices)):
                        right+=1
                        if(prices[right] - prices[left]  > profit):
                            profit = prices[right] - prices[left]

        return profit

           



        