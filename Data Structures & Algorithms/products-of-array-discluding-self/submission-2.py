class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        a_prefix = 1
        postfix = []
        a_postfix = 1
        res = []

        for i in range(len(nums)):
            a_prefix = nums[i] * a_prefix
            prefix.append(a_prefix)
        for j in range(len(nums)-1,-1,-1):
            a_postfix = nums[j] * a_postfix
            postfix.append(a_postfix)
        postfix = postfix[::-1]

        for k in range(len(nums)):
            if k==0:
                res.append(postfix[k+1])
            elif k==len(nums)-1:
                res.append(prefix[k-1])
            else:
                res.append(prefix[k-1] * postfix[k+1])
        
        return res


        


