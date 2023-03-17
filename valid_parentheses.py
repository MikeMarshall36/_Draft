def br_check(text: str) -> bool:
    opening_br, closing_br = "(", ")"
    br_stack = []
    for character in text:
        if character == opening_br:
            br_stack .append(opening_br.index(character))
        elif character == closing_br:
            if len(br_stack) > 0 and br_stack[-1] == closing_br.index(character):
                br_stack .pop()
            else:
                return False

    return not br_stack


print(br_check('(())((()())())'))
print(br_check('()'))
print(br_check('('))
print(br_check(')(()))'))
