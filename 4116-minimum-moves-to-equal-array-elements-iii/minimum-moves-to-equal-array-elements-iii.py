class Solution:
  def minMoves(self, nums: List[int]) -> int:
    mx = max(nums)
    s = sum(nums)
    return mx * len(nums) - s
