from typing import List


class Solution:
    # solution 1, using Sort, Time: O(n^2) Space O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    # solution 2, using Set, Time: O(1), Space O(n)
    def containsDuplicate2(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    s = Solution()
    print(s.containsDuplicate2(nums))
