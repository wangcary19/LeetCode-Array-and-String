# February 2nd, 2024
def moveZeroes(self, nums: List[int]) -> None:
    zeroes = nums.count(0)
    nums[:] = [x for x in nums if x != 0]
    for i in range(0, zeroes):
        nums.append(0)