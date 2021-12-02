class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i<len(nums):
            if nums[j]==0:
                nums.pop(nums.index(0))
                nums.append(0)
            else:
                j+=1
            i+=1
        return nums
