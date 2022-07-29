#TC : O(n)
#SC : O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rp = 1 #running product
        result = [0]*len(nums)
        result[0]=1
      
        
        for i in range(1,len(nums)):
            rp = result[i-1]*nums[i-1]
            result[i] = rp
        
        rp = 1
        for i in range(len(nums)-2,-1,-1):
            rp = rp*nums[i+1]
            result[i] = result[i]*rp
        
        return result