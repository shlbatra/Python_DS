from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n:int) -> None:
        # Ex. m = 6 , n =3
        # 1, 2, 3, 0, 0, 0
        # 2, 5, 6

        # 3 ptrs l1 end of list1, l2 end of list2, l11 where actual numbers end in list 1

        last = (m+n-1)

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]: # when nums1 number greater than equal to num2 number
                nums1[last] = nums1[m-1]
                m = m-1

            else: # when nums1 number smaller than nums2 number
                nums1[last] = nums2[n-1]
                n = n-1

            last = last-1

        # fill nums1 with leftover elements in n -> as if smallest element in second array
        if n>0:
            nums1[last] = nums2[n-1]
            last = last-1
            n = n - 1
        return nums1
    
obj1 = Solution()
print(obj1.merge([2, 2, 3, 0, 0, 0],3,[1, 4, 6],3))