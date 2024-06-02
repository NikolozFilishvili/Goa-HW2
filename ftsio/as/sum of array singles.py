def repeats(arr):

    nums = set()

    for i in arr:
        if i in nums:
            nums.remove(i)
        else:
            nums.add(i)
    return sum(nums)

print(repeats([2,4,4,5,6,6]))