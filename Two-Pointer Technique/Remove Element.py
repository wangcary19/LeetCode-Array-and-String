# January 24th, 2024

def removeElement(self, nums: List[int], val: int) -> int:
    i = 0

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            continue
        else:
            i += 1
            continue

    return len(nums)