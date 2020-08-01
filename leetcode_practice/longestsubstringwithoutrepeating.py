class Solution:
    def lengthoflongestsubstring(self, s):
        sls = len(set(s))
        slen = len(s)
        if slen < 1:
            return 0
        else:
            max_len = 1

        for i in range(slen):
            for j in range(i+max_len+1, i+sls+1):
                curr = s[i:j]
                curr_len = len(curr)
                if len(set(curr)) != curr_len:
                    break
                else:
                    if curr_len > max_len:
                        max_len = curr_len
        return max_len
