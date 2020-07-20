class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)
        def dfs(remains, stack):
            if remains == 0:
                result.append(stack)
            else:
                for item in candidates:
                    if remains < item:
                        break
                    elif stack and item < stack[-1]:
                        continue
                    else:
                        dfs(remains-item, stack+[item])
        dfs(target, [])
        return result
