# February 2nd, 2024
def removeDuplicates(self, nums: List[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)