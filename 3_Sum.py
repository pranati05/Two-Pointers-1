class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        for i in range(len(nums)):
            numsSet = set()
            for j in range(i+1, len(nums)):
                comp = 0 - (nums[i] + nums[j])
                if comp in numsSet:
                    sortedTriplet = sorted([comp, nums[i], nums[j]])
                    result.add(tuple(sortedTriplet))
                numsSet.add(nums[j])
        output = []

        for x in result:
            output.append(list(x))
#Time - O(N2)
#Space - O(N)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif target < 0:
                    left += 1
                else:
                    right -= 1
        return result
#Time - O(N2)
#Space - O(1)