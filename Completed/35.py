def searchInsert(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        return sorted(nums).index(target)


print(searchInsert(nums=[1,3,7,6], target=5))