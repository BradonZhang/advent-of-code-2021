with open('in/1.txt') as f:
    nums = list(map(int, f.readlines()))

# Part 1
print(sum(nums[i] > nums[i - 1] for i in range(1, len(nums))))

# Part 2
windows = [nums[i] + nums[i - 1] + nums[i - 2] for i in range(2, len(nums))]
print(sum(windows[i] > windows[i - 1] for i in range(1, len(windows))))
