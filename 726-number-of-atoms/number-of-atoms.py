from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1

            elif formula[i] == ')':
                i += 1

                num = 0
                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                if num == 0:
                    num = 1

                current = stack.pop()

                for atom, count in current.items():
                    stack[-1][atom] += count * num

            else:
                # Read atom name
                atom = formula[i]
                i += 1

                while i < n and formula[i].islower():
                    atom += formula[i]
                    i += 1

                # Read atom count
                num = 0
                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1

                if num == 0:
                    num = 1

                stack[-1][atom] += num

        result = []

        for atom in sorted(stack[-1]):
            result.append(atom)

            if stack[-1][atom] > 1:
                result.append(str(stack[-1][atom]))

        return ''.join(result)
