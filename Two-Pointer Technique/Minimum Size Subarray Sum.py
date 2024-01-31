# January 30th, 2024

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    if target in nums:
        return 1
    elif sum(nums) == target:
        return len(nums)
    elif sum(nums) < target:
        return 0
    else:
        s = 0
        l_idx = 0
        out = len(nums)

        for i in range(0, len(nums)):  # window right anchor
            s += nums[i]
            while (s >= target):  # shrink left windowframe until not valid
                out = min(out, i - l_idx + 1)
                s -= nums[l_idx]
                l_idx += 1
            # end-while
        # end-for

        return out