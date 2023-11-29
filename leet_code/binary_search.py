class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        cpt1 = 0
        cpt2 = 0
        while len(nums) > 1:
            size = len(nums)
            nums1 = nums[: size // 2]
            nums2 = nums[size // 2 :]
            if nums1[-1] < target and nums2[0] > target:
                return -1
            elif nums1[-1] > target:
                nums = nums1
            elif nums2[0] < target:
                cpt2 += size // 2
                cpt1 += size // 2
                nums = nums2
            elif nums1[-1] == target:
                return cpt1 + size // 2 - 1
            else:
                return cpt2 + size // 2
        if nums[0] == target:
            return cpt2
        else:
            return -1
