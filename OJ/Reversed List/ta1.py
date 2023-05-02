def reverse(L):
    rL = L[::-1]
    for i, e in enumerate(rL):
        if type(e) is list:
            rL[i] = reverse(e)
    return rL