def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    lst = sorted(nums1 + nums2)
    lst_median = len(lst) // 2
    lists = [lst[0:lst_median], lst[lst_median:]]
    
    if len(lst) % 2 == 0:
        return float((lists[0][-1] + lists[1][0]) / 2)
    else:
        return float(lists[1][0])



print(findMedianSortedArrays([1,2,3,4,5], [6,7,8,9,10,11,12,13,14,15,16, 17]))