def reverse_bits(num: int) -> int:
    res = 0
    for _ in range(32):
        bit = num & 1
        res = (res << 1) | bit
        num = num >> 1
    return res

def hamming_weight(n: int) -> int:
    res = 0
    for _ in range(32):
        bit = n & 1
        res += bit
        n = n >> 1
    return res




def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def single_number(nums: list[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res

def hex_to_binary_str(hex_str: str) -> str:
    n = int(hex_str, 16)
    return f"{n:0{len(hex_str) * 4}b}"


def format_report(n: int) -> str:
    return (
        f"Decimal: {n:d}\n"
        f"Binary:  {n:032b}\n"
        f"Octal:   {n:o}\n"
        f"Hex:     {n:x}\n"
        f"Hex:     {n:X}"
    )




if __name__ == "__main__":
    assert reverse_bits(43261596) == 964176192
    assert hamming_weight(11) == 3          # 1011
    assert is_power_of_two(16) is True
    assert is_power_of_two(18) is False
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert hex_to_binary_str('a3') == '10100011'
    print(single_number([4, 1, 2, 1, 2]))
    print(format_report(255))
