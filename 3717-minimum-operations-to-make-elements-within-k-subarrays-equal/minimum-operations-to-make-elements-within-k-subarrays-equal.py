import heapq
from collections import Counter

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        
        # -------------------------------------------------------------
        # Part 1: Calculate the median equalization cost for each window of size x
        # -------------------------------------------------------------
        window_costs = [0] * n
        
        # Two heaps to track elements in the window:
        # left_heap (max-heap) tracks the smaller half
        # right_heap (min-heap) tracks the larger half
        left_heap = []
        right_heap = []
        
        left_sum = 0
        right_sum = 0
        
        left_count = 0
        right_count = 0
        
        # Lazy deletion dictionary for tracking elements out of window
        to_delete = Counter()
        
        def clean_heap(heap, is_left):
            # Remove elements that are no longer part of the current sliding window
            while heap:
                val = heap[0] if not is_left else -heap[0]
                if to_delete[val] > 0:
                    to_delete[val] -= 1
                    heapq.heappop(heap)
                else:
                    break

        for i, num in enumerate(nums):
            # Insert the new element into the correct heap
            if not left_heap or num <= -left_heap[0]:
                heapq.heappush(left_heap, -num)
                left_sum += num
                left_count += 1
            else:
                heapq.heappush(right_heap, num)
                right_sum += num
                right_count += 1
                
            # Remove out-of-window element if window size exceeds x
            if i >= x:
                out_num = nums[i - x]
                to_delete[out_num] += 1
                if out_num <= -left_heap[0] if left_heap else False:
                    left_sum -= out_num
                    left_count -= 1
                else:
                    right_sum -= out_num
                    right_count -= 1
            
            # Rebalance heaps so left_heap gets the extra element if count is odd
            # Condition: left_count == right_count or left_count == right_count + 1
            clean_heap(left_heap, True)
            clean_heap(right_heap, False)
            
            while left_count > right_count + 1:
                val = -heapq.heappop(left_heap)
                heapq.heappush(right_heap, val)
                left_sum -= val
                right_sum += val
                left_count -= 1
                right_count += 1
                clean_heap(left_heap, True)
                
            while left_count < right_count:
                val = heapq.heappop(right_heap)
                heapq.heappush(left_heap, -val)
                right_sum -= val
                left_sum += val
                right_count -= 1
                left_count += 1
                clean_heap(right_heap, False)
                
            # Heaps are clean and balanced at the current window's end
            clean_heap(left_heap, True)
            clean_heap(right_heap, False)
            
            # Calculate cost once we have processed a full window of size x
            if i >= x - 1:
                median = -left_heap[0]
                # L1 Cost calculation formula using prefix/heap sums:
                # (median * left_count - left_sum) + (right_sum - median * right_count)
                cost = (median * left_count - left_sum) + (right_sum - median * right_count)
                window_costs[i] = cost

        # -------------------------------------------------------------
        # Part 2: Dynamic Programming to select K non-overlapping windows
        # -------------------------------------------------------------
        # dp[j] represents the minimum operations to pick `j` non-overlapping windows
        # Initialize with infinity, dp[0] = 0 (cost of picking 0 windows)
        dp = [float('inf')] * (k + 1)
        dp[0] = 0
        
        # To avoid over-allocating states or looking backwards beyond bounds, 
        # we can build a 2D-like structural approach or match history per index.
        # dp_states stores the optimal DP array at each index up to `i`
        dp_states = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp_states[0][0] = 0
        
        for i in range(1, n + 1):
            # Choice A: Do not select a window ending at index i-1
            for j in range(k + 1):
                dp_states[i][j] = dp_states[i - 1][j]
                
            # Choice B: Select a window ending at index i-1 (starts at i-x)
            if i >= x:
                cost = window_costs[i - 1]
                for j in range(1, k + 1):
                    if dp_states[i - x][j - 1] != float('inf'):
                        dp_states[i][j] = min(dp_states[i][j], dp_states[i - x][j - 1] + cost)
                        
        return dp_states[n][k]
