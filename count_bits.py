def count_bits(num: int) -> int:
    bin_string = (bin(num)[2:])
    return bin_string.count('1')


print(count_bits(1234))
print(count_bits(2))
