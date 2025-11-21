# 15. 3Sum
# https://leetcode.com/problems/3sum/


def threeSum(nums: list[int]) -> list[list[int]]:
    if len(nums) < 3:
        return []

    triplets = []

    nums = sorted(nums)

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            triplet = [nums[i], nums[left], nums[right]]
            triplet_sum = sum(triplet)

            if triplet_sum < 0: 
                left += 1
            elif triplet_sum > 0: 
                right -= 1
            else:
                triplets.append(triplet)

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                
    return triplets


print(threeSum(nums=[13,4,-6,-7,-15,-1,0,-1,0,-12,-12,9,3,-14,-2,-5,-6,7,8,2,-4,6,-5,-10,-4,-9,-14,-14,12,-13,-7,3,7,2,11,7,9,-4,13,-6,-1,-14,-12,9,9,-6,-11,10,-14,13,-2,-11,-4,8,-6,0,7,-12,1,4,12,9,14,-4,-3,11,10,-9,-8,8,0,-1,1,3,-15,-12,4,12,13,6,10,-4,10,13,12,12,-2,4,7,7,-15,-4,1,-15,8,5,3,3,11,2,-11,-12,-14,5,-1,9,0,-12,6,-1,1,1,2,-3]))
