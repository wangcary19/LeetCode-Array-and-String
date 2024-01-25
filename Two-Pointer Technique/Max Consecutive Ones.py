# January 24th, 2024
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    max = 0
    accrued = 0

    for i in nums:
        if i == 0:
            if accrued > max:
                max = accrued
                accrued = 0
            else:
                accrued = 0
        else:
            accrued += 1

    if accrued > max:
        return accrued
    else:
        return max