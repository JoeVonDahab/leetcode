import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        n = 0
        m = 0
        total_len = len(nums1) + len(nums2)
        is_odd = False 
        if total_len % 2 != 0:
            is_odd = True
        mid_point = total_len // 2
        while len(merged) <= mid_point:
            if n < len(nums1) and (m >= len(nums2) or nums1[n] <= nums2[m]):
                merged.append(nums1[n])
                n += 1 
            else: 
                merged.append(nums2[m])
                m += 1
        if is_odd:
            return float(merged[mid_point])
        else: 
            return float(merged[mid_point] + merged[mid_point-1]) /2 

