T = int(input())
for t in range(T):
    target = int(input())
    nums = [int(s) for s in input().split()]

    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f'Case #{t+1}: {[i, j]}')
