class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        m = {}
        for i in range(0, len(nums)):
            if target - nums[i] in m:
                res.append(i)
                res.append(m.get(target - nums[i]))
                break
            m[nums[i]] = i
        return res