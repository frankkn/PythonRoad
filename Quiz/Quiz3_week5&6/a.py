# LeetCode 1200. Minimum Absolute Difference
class Solution:
  def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    _min = 1e6
    ans = []
    for i in range(0, len(arr)-1):
      if abs(arr[i]-arr[i+1]) <= _min:
        _min = abs(arr[i]-arr[i+1])
    for i in range(0, len(arr)-1):
      if abs(arr[i]-arr[i+1]) == _min:
        ans.append([arr[i], arr[i+1]])
    return ans