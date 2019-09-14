

class Solution:

    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1_i, n2_i, t_i = m - 1, n - 1, m + n - 1
        while n1_i >= 0 and n2_i >= 0:
            if nums1[n1_i] >= nums2[n2_i]:
                nums1[t_i] = nums1[n1_i]
                n1_i -= 1
            else:
                nums1[t_i] = nums2[n2_i]
                n2_i -= 1
            t_i -= 1

        if n2_i >= 0:
            nums1[:n2_i + 1] = nums2[:n2_i + 1]
