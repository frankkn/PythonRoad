def permute(nums):
    if len(nums) == 1:
        return [nums]
    perm = []
    for candi in nums:
        sub_perm = permute([n for n in nums if n != candi])
        for p in sub_perm:
            perm.append([candi] + p)
    return perm