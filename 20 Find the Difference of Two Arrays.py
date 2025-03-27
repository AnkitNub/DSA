class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans0 = []
        ans1 = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in ans0:
                ans0.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in ans1:
                ans1.append(nums2[i])
        return [ans0,ans1]