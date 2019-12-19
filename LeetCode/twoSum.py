class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            if target - nums[i] not in map:
                map[nums[i]] = i
            else:
                return [map[target - nums[i]], i]