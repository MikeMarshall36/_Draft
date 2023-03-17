string_1 = "the-stealth-warrior"
string_2 = "The_Stealth_Warrior"
string_3 = "The_Stealth-Warrior"
string_4 = "The Stealth Warrior"


def to_camel_case(text: str) -> str:
    delimiters = ['-', '_']
    text = text.replace('_', ' ').replace('-', ' ')
    text = text.split(' ')
    for i in range(1, len(text)):
        text[i] = text[i].title()
    return ''.join(text)


print(to_camel_case(string_1))
print(to_camel_case(string_2))
print(to_camel_case(string_3))
print(to_camel_case(string_4))
