def duplicate_count(text: str) -> int:
    text = text.casefold()
    duplicates = 0
    l_checked = []
    for i in range(len(text)):
        if text.count(text[i]) > 1 and text[i] not in l_checked:
            l_checked.append(text[i])
            duplicates += 1
    return duplicates


print(duplicate_count('abcdeaB'))
