def double_split(s: str) -> list:
    res = []
    if len(s) % 2 == 0:
        return [s[i:i+2] for i in range(0, len(s), 2)]
    else:
        s += '_'
        return [s[i:i+2] for i in range(0, len(s), 2)]


print(double_split('asdfads'))
print(double_split('asdfadsf'))
