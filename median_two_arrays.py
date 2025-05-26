import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        n = 0
        m = 0
        added_last_n = False
        added_last_m = False
        new_array = []
        is_it_odd = False
        middle_point = total_len / 2
        if total_len % 2 != 0:
            is_it_odd = True
        else:
            middle_point = int(middle_point)

        
         
        if not nums1:
            if is_it_odd:
                rounded = math.ceil(middle_point)
                return nums2[rounded-1]
            else:
                one = float(nums2[middle_point])
                two = float(nums2[middle_point-1])
                three = one + two
                return three / 2
        if not nums2: 
            if is_it_odd:
                rounded = math.ceil(middle_point)
                return nums1[rounded-1]
            else:
                one = float(nums1[middle_point])
                two = float(nums1[middle_point-1])
                three = one + two
                return three / 2

        for i in range(total_len):
            if nums1[n] <= nums2[m] and added_last_n != True:
                new_array.append(nums1[n])
                
                if len(nums1) - 1 == n:
                    added_last_n = True
                else:
                    n += 1
            elif added_last_m == False:
                new_array.append(nums2[m])
                if len(nums2) - 1 == m:
                    added_last_m = True
                else:
                    m+= 1
            else:
                new_array.append(nums1[n])
                
                if len(nums1) - 1 == n:
                    added_last_n = True
                else:
                    n += 1
            if i + 1 > middle_point and is_it_odd:
                return new_array[i]
            if i  == middle_point:
                    one = float(new_array[i])
                    two = float(new_array[i-1])
                    three = one + two
                    return three / 2
