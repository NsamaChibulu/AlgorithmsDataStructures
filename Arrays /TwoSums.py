#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.


class Solution(object):
    def TwoSums(self,nums,target):

        '''Type nums : list(integers)
        Type target : int 
        range type : list(integers)'''

        for i in range(len(nums)):
            element = target - nums[i]
            try:
                pos = nums.index(element)
                if pos == i:
                    continue
                if(nums[i] + nums[pos]) == target:
                    return [i,pos]
            except:
                continue

