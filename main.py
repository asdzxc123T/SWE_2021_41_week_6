def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums) - i):
            if i == i + j:
                continue
            if nums[i] + nums[i + j] == target:
                print("Output: [" + str(i) + ", " + str(i + j) + "]")
                return

twoSum([2, 7, 11, 15], 9)
twoSum([3, 2, 4], 6)
twoSum([3, 3], 6)