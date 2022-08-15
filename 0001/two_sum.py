class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        # print(l)
        for i in range(0, l-1):
            for j in range(i+1, l):
                # print(nums[i], nums[j])
                if target == nums[i] + nums[j]:
                    return [i,j]
