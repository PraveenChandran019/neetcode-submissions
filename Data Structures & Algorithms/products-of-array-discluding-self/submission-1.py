class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        l = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    a = nums[j] * a
            l.append(a)
            a = 1
        return l