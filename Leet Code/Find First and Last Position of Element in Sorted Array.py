class Solution(object):
    
    def first_obs(self, nums, target) : 
        begin = 0
        end = len(nums)
        
        while begin < end : 
            middle = (end+begin)/2
            if nums[middle]>= target : 
                end = middle
            else : 
                begin = middle + 1
        return begin
    
    def last_obs(self, nums, target) : 
        begin = 0
        end = len(nums)
        
        while begin < end : 
            middle = (end+begin)/2
            if nums[middle] > target : 
                end = middle
            else : 
                begin = middle + 1
        return begin
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) == 0 :
            return ([-1, -1])
        begin = self.first_obs(nums, target)
        end = self.last_obs(nums, target) - 1
        if begin == len(nums) or nums[begin] != target:
            return [-1,-1]
        
        return [begin, end]
