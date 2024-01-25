# January 24th, 2024
def arrayPairSum(self, nums: List[int]) -> int:
    nums = sorted(nums)
    return sum(nums[2 * i] for i in range(0, int(len(nums) / 2)))