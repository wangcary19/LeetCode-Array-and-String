# January 24th, 2024

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    if len(numbers) == 2:
        return [1, 2]
    else:
        i = 0
        j = len(numbers) - 1
        while True:
            if numbers[i] + numbers[j] == target:
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
                continue
            else:
                j -= 1
                continue
    return [i + 1, j + 1]