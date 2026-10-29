import sys

# Increase recursion depth for deep tree structures
sys.setrecursionlimit(300000)

class FenwickTreeRangeXor:
    """
    Fenwick Tree (Binary Indexed Tree) that supports:
    1. Range XOR update: update_range(l, r, val)
    2. Point query: query(idx)
    This is achieved by applying point XOR updates at 'l' and 'r + 1'.
    """
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 2)

    def _add(self, idx: int, val: int):
        idx += 1  # 1-based indexing for Fenwick Tree
        while idx <= self.size + 1:
            self.tree[idx] ^= val
            idx += idx & (-idx)

    def update_range(self, l: int, r: int, val: int):
        if l > r:
            return
        self._add(l, val)
        self._add(r + 1, val)

    def query(self, idx: int) -> int:
        idx += 1
        res = 0
        while idx > 0:
            res ^= self.tree[idx]
            idx -= idx & (-idx)
        return res


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # 1. Build adjacency list for the tree
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. Setup structures for Binary Lifting (LCA) and Euler Tour
        LOG = n.bit_length()
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        # Array to store the path mask from root to node `i`
        root_to_node_mask = [0] * n
        
        # Helper mapping for character masks
        def get_char_mask(char: str) -> int:
            return 1 << (ord(char) - ord('a'))

        # 3. DFS to compute depths, binary lifting table, and Euler Tour intervals
        def dfs(node: int, parent: int, current_mask: int):
            nonlocal timer
            tin[node] = timer
            timer += 1
            
            # Incorporate the current node's character mask
            next_mask = current_mask ^ get_char_mask(s[node])
            root_to_node_mask[node] = next_mask
            
            up[node][0] = parent
            for i in range(1, LOG):
                up[node][i] = up[up[node][i - 1]][i - 1]
                
            for neighbor in adj[node]:
                if neighbor != parent:
                    depth[neighbor] = depth[node] + 1
                    dfs(neighbor, node, next_mask)
                    
            tout[node] = timer - 1

        # Initialize DFS from root node 0
        dfs(0, 0, 0)

        # 4. Helper function to find the Lowest Common Ancestor (LCA)
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            
            # Bring both nodes to the same depth level
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
                    
            if u == v:
                return u
                
            # Lift both nodes together until they meet below their LCA
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
                    
            return up[u][0]

        # 5. Initialize the Fenwick tree with base root-to-node masks
        # Since we use an Euler Tour, a range update on node `i`'s subtree
        # corresponds to updating indices from tin[i] to tout[i].
        # We populate the Fenwick Tree by simulating initial range configurations.
        bit = FenwickTreeRangeXor(timer)
        
        # Create an array tracking the current active character at each node
        current_chars = list(s)
        
        # Build the initial state inside the Fenwick Tree
        # An elegant way is to apply the node's individual character mask to its entire subtree
        for i in range(n):
            mask = get_char_mask(s[i])
            bit.update_range(tin[i], tout[i], mask)

        # 6. Process Queries
        ans = []
        for query in queries:
            parts = query.split()
            
            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]
                
                old_char = current_chars[u]
                if old_char != new_char:
                    # XOR out the old character mask and XOR in the new one
                    xor_diff = get_char_mask(old_char) ^ get_char_mask(new_char)
                    # Updating a node affects its entire subtree in the flattened layout
                    bit.update_range(tin[u], tout[u], xor_diff)
                    current_chars[u] = new_char
                    
            elif parts[0] == "query":
                u = int(parts[1])
                v = int(parts[2])
                
                lca = get_lca(u, v)
                
                # Fetch dynamically computed root-to-node path masks from Fenwick Tree
                mask_u = bit.query(tin[u])
                mask_v = bit.query(tin[v])
                
                # Path expression: Mask(u) ^ Mask(v) ^ Mask(LCA's character)
                # Note: mask_u ^ mask_v cancels out everything above LCA, except one copy of LCA's path.
                # To get only the path elements inclusive, we adjust with LCA's single character node mask.
                lca_char_mask = get_char_mask(current_chars[lca])
                path_mask = mask_u ^ mask_v ^ lca_char_mask
                
                # A string can be rearranged into a palindrome if it has at most one odd-frequency character.
                # In our bitmask, this means at most 1 bit is set.
                # Check if path_mask is 0 or a perfect power of 2:
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)

        return ans
