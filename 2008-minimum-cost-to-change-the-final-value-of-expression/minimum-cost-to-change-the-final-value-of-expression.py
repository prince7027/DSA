class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        # Elements in the stack will be either:
        # - An operator character: '&', '|', '('
        # - A tuple: (val, cost) representing the expression's evaluated state
        stack = []
        
        def evaluate_top():
            # Performs the operation sitting at the top of the stack
            # between the two surrounding values
            right_val, right_cost = stack.pop()
            op = stack.pop()
            left_val, left_cost = stack.pop()
            
            if op == '&':
                if left_val == 1 and right_val == 1:
                    # 1 & 1 = 1 -> Needs to become 0
                    # Options: flip left to 0 (left_cost) OR flip right to 0 (right_cost)
                    new_val, new_cost = 1, min(left_cost, right_cost)
                elif left_val == 0 and right_val == 0:
                    # 0 & 0 = 0 -> Needs to become 1
                    # Must flip '&' to '|' AND flip either left or right to 1
                    new_val, new_cost = 0, 1 + min(left_cost, right_cost)
                else:
                    # 1 & 0 = 0 or 0 & 1 = 0 -> Needs to become 1
                    # Simply flip '&' to '|', then 1 | 0 becomes 1 automatically
                    new_val, new_cost = 0, 1
            else:  # op == '|'
                if left_val == 0 and right_val == 0:
                    # 0 | 0 = 0 -> Needs to become 1
                    new_val, new_cost = 0, min(left_cost, right_cost)
                elif left_val == 1 and right_val == 1:
                    # 1 | 1 = 1 -> Needs to become 0
                    new_val, new_cost = 1, 1 + min(left_cost, right_cost)
                else:
                    # 1 | 0 = 1 or 0 | 1 = 1 -> Needs to become 0
                    # Simply flip '|' to '&', then 1 & 0 becomes 0 automatically
                    new_val, new_cost = 1, 1
                    
            stack.append((new_val, new_cost))

        for char in expression:
            if char in "(&|":
                stack.append(char)
            elif char == ")":
                # The stack top contains the group result. 
                # Pop it, clear the '(' beneath it, and put the result back.
                res = stack.pop()
                stack.pop()  # pop '('
                stack.append(res)
                # If there's an active operator ready before this group, execute it
                if len(stack) >= 3 and stack[-2] in ('&', '|'):
                    evaluate_top()
            else:
                # Leaf element ('0' or '1')
                # Cost to toggle a single digit directly is always 1
                val = int(char)
                stack.append((val, 1))
                # If there's an active operator ready, execute it immediately
                if len(stack) >= 3 and stack[-2] in ('&', '|'):
                    evaluate_top()
                    
        return stack[0][1]
