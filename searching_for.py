arr = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
for num in arr:
    if arr.count(num) % 2 != 0:
        print(num)


def find_it(seq):
    return [num for num in seq if seq.count(num) % 2 != 0][0]


print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
