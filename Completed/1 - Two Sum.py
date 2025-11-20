# 1. Two Sum
# https://leetcode.com/problems/two-sum/


def twoSum(nums: list[int], target: int) -> list[int]:
    # Going through all the items in the list
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            print(nums[i], nums[j], sum([nums[i], nums[j]]))
            if nums[i] + nums[j] == target: # If the sum of the elements is target
                return [i, j] # Returning the list of element indexes

    return []


nums = [3,2,3]
target = 6

print(twoSum(nums=nums, target=target))
