def generate_hashtag(text: str) -> str:
    if len(text) == 0 or len(text) > 140:
        return False
    else:
        text = text.lower().strip().split(' ')
        text = [item.title() for item in text]
        hashtag = '#'+''.join(text)
    return hashtag


print(generate_hashtag(' Hello there thanks for trying my Kata'))
