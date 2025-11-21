# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/


def reverse(x: int) -> int:
    if str(x)[0].isdigit():
        return int(str(x)[::-1]) if int(str(x)[::-1]) <= 2**31 -1 else 0
    else:
        return -1 * int(str(x)[::-1][:-1]) if -1 * int(str(x)[::-1][:-1]) >= -2**31 -1 else 0


numbers = [1, 2, -3, -10, -111, 1234, -123]

for n in numbers:
    print(f"Number {n}: ", reverse(n))