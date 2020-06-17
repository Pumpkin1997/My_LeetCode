# #53最大子序和
# #暴力搜索 O(n²)
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         l=len(nums)
#         max=nums[0]  
#         for i in range (0,l):
#             sum=0
#             for j in range (0,l-i):
#                 sum+=nums[i+j]
#                 if sum > max:
#                     max=sum
#         return max
# a=Solution()
# nums=[-2,1]
# result=a.maxSubArray(nums)
# print(result)

# #动态规划 O(n)
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         l=len(nums)
#         max=nums[0]  
#         for i in range (0,l):
#             sum=0
#             for j in range (0,l-i):
#                 sum+=nums[i+j]
#                 if sum > max:
#                     max=sum
#         return max
# a=Solution()
# nums=[-2,1]
# result=a.maxSubArray(nums)
# print(result)

#分治
class Solution(object):
    def __init__(self,nums):
        self.nums=nums

    def maxSubArray(self, nums, left, right):
        """
        :type nums: List[int]
        :rtype: int
        :type left,right: int
        """
        leftsum=0
        rightsum=0
        maxleftsum=0
        maxrightsum=0

        #最大和子序列在左半边或右半边
        mid=int((left+right)/2)
        # 递归出口，只剩一个数
        if (left==right):
            return nums[left]

        #左半边递归
        leftresult= self.maxSubArray(nums,left,mid)
        #右半边递归
        rightresult= self.maxSubArray(nums,mid+1,right)

        #最大和子序列横跨两边
        for i in range(mid,left-1,-1):
            leftsum+=nums[i]
            if leftsum>maxleftsum:
                maxleftsum=leftsum
        for j in range(mid+1,right+1,1):
            rightsum+=nums[j]
            if rightsum>maxrightsum:
                maxrightsum=rightsum
            
        return max(leftresult,rightresult,maxleftsum+maxrightsum)
        
nums=[-2,1,-3,4,-1,2,1,-5,4]
a=Solution(nums)
result=a.maxSubArray(nums,0,len(nums)-1)
print(result)
