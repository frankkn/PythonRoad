#!/usr/bin/env python3

# Mutation(list only) vs Non-mutation(all)
L = [1,2,3,4,5]
S = [1,2,3,4,5]
L.sort() 
S = sorted(S)

L.reverse() 
S = list(reversed(S))
S = S[::-1]

L.extend([1,2,3])
L += [1,2,3]
S = S + [1,2,3]

del(L[1])
S = S[:1] + S[2:]

L.pop()
S = S[:-1]