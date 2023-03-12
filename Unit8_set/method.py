#!/usr/bin/env python3

# S.add(e): add e to the set
# S |= {e}

# S.clear(): clear elements from set
# S -= S

# S.pop(): remove arbitrary element
# S -= some random e

# S.remove(e): remove element e, error if e is not in S
# S -= {e}

# S.discard(e): remove element e, no error in all cases
# S -= {e}

# S.update(T): update S with union with T i.e., S |= T
# S |= T

# Mutation vs Non-Mutation Methods of set class
# S.union(T) S | T
# S.update(T) S |= T

# S.difference(T) S - T
# S.difference_update(T) S -= T

# S.symmetric_difference(T) S ^ T
# S.symmetric_difference_update(T) S ^= T