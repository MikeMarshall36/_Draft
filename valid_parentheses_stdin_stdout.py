import sys


def valid_parentheses(text, brackets="()[]{}"):
    if len(text) == 0:
        return 'Bruh'
    opening, closing = brackets[::2], brackets[1::2]
    stack = []
    for character in text:
        if character in opening:
            stack.append(opening.index(character))
        elif character in closing:
            if len(stack) > 0 and stack[-1] == closing.index(character):
                stack.pop()
            else:
                return False

    return not stack


for line in sys.stdin:
    res = valid_parentheses(line)
    if res == False:
        sys.stdout.write('Bruh')
    else:
        sys.stdout.write('Nice')

print(valid_parentheses('([{}]())'))
print(valid_parentheses('()((}}'))
