def isBalanced(s):
    openers =  deque()
    brackets = {")": "(", "]":"[", "}":"{"}
    for c in s:
        if c in {"(","[", "{"}:
            openers.append(c)
        else:
            if not openers or brackets[c]!=openers.pop():
                return "NO"
    return "NO" if openers else "YES"