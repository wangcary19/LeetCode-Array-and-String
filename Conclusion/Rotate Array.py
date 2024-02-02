# February 1st, 2024
def rotate(self, nums: List[int], k: int) -> None:

    k = k % len(nums)  # parse k to reduce motions

    to_back = nums[0:len(nums) - k]
    new_front = nums[len(nums) - k:]
    nums.clear()
    nums += new_front
    nums += to_back