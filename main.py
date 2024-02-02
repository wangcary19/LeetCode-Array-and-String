# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(int(3/2))

    min_len = len(nums)
    for i in range(1, len(nums) - 1):  # list slice size
        for j in range(0, len(nums) - i + 1):  # slice start
            # print("Checking " + str(nums[j:j + i]) + ", i is " + str(i) + ", j is " + str(j))
            if sum(nums[j:j + i]) >= target and i < min_len:
                min_len = i
                # print("min_len set to " + str(min_len))
            else:
                continue
    # end-for
    return min_len

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
