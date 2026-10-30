import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        # Build the adjacency list: adj[u] = [(v, weight), ...]
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # dist[u][c] stores the minimum cost to reach node `u` 
        # where the path ends with exactly `c` consecutive identical characters.
        # c ranges from 1 to k.
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        # Priority Queue stores tuples of: (current_cost, current_node, consecutive_count)
        # Starting at node 0, its own label counts as 1 consecutive character.
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            d, u, c = heapq.heappop(pq)
            
            # If we found a shorter path to this state already, skip it
            if d > dist[u][c]:
                continue
                
            # If we reached the target node, return the cost immediately
            if u == n - 1:
                return d
                
            for v, w in adj[u]:
                # Determine the new consecutive count for node `v`
                if labels[u] == labels[v]:
                    new_c = c + 1
                else:
                    new_c = 1
                    
                # If the consecutive sequence exceeds the limit `k`, this path is invalid
                if new_c > k:
                    continue
                    
                # Relaxation step
                if d + w < dist[v][new_c]:
                    dist[v][new_c] = d + w
                    heapq.heappush(pq, (d + w, v, new_c))
                    
        return -1
