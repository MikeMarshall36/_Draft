l = [1, 2, 'a', 'b']


def filter_list(input_list: list) -> list:
    res = []
    for item in input_list:
        if isinstance(item, int):
            res.append(item)
    print(res)
    return res


filter_list(l)
