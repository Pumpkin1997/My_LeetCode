# #动态规划ver1
# class Solution(object):
#     def maxProfit(self,prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         maxprofit=0
#         for i in range(len(prices)-1,0,-1):
#             minprices = min (prices[0:i])
#             current_profit=prices[i]- minprices
#             if current_profit > maxprofit:
#                 maxprofit = current_profit
#         return maxprofit

# prices=[7,1,5,3,6,4]
# a=Solution()
# result=a.maxProfit(prices)
# print(result)


#动态规划优化ver2
class Solution(object):
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit=0
        minprices=float('inf')
        for i in range(0,len(prices)):
            minprices = min (minprices,prices[i])
            maxprofit = max (maxprofit,prices[i]- minprices)
        return maxprofit

prices=[7,1,5,3,6,4]
a=Solution()
result=a.maxProfit(prices)
print(result)

