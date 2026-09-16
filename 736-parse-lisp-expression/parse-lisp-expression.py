class Solution:
    def evaluate(self, expression: str) -> int:
        def eval_expr(s, env):
            if s[0] != '(':
                try:
                    return int(s)
                except:
                    return env[s]

            s = s[1:-1]

            parts = []
            cur = []
            level = 0

            for c in s:
                if c == '(':
                    level += 1
                elif c == ')':
                    level -= 1

                if c == ' ' and level == 0:
                    if cur:
                        parts.append(''.join(cur))
                        cur = []
                else:
                    cur.append(c)

            if cur:
                parts.append(''.join(cur))

            op = parts[0]

            if op == "add":
                return eval_expr(parts[1], env) + eval_expr(parts[2], env)

            if op == "mult":
                return eval_expr(parts[1], env) * eval_expr(parts[2], env)

            if op == "let":
                new_env = env.copy()

                i = 1
                while i < len(parts) - 1:
                    var = parts[i]
                    value = eval_expr(parts[i + 1], new_env)
                    new_env[var] = value
                    i += 2

                return eval_expr(parts[-1], new_env)

        return eval_expr(expression, {})
