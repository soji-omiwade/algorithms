'''
1 2 2 2 2 3
1 2 3 4 5
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        idx1 = idx2 = 0
        res = []
        m, n = len(nums1), len(nums2)
        while idx1 < m and idx2 < n:
            if nums1[idx1] == nums2[idx2]:
                if not res or nums1[idx1] != res[-1]:
                    res.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return res