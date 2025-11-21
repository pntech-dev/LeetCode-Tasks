def reverse(x: int) -> int:
    # string = str(x)[::-1]

    # sign = 1 if string[-1].isdigit() else -1

    # if sign == 1:
    #     return int(string) if int(string) <= 2**31 - 1 else 0
    # elif sign == -1:
    #     return -1 * int(string[:-1]) if -1 * int(string[:-1]) >= -2**31 else 0

    if str(x)[0].isdigit():
        return int(str(x)[::-1]) if int(str(x)[::-1]) <= 2**31 -1 else 0
    else:
        return -1 * int(str(x)[::-1][:-1]) if -1 * int(str(x)[::-1][:-1]) >= -2**31 -1 else 0


numbers = [1, 2, -3, -10, -111, 1234, -123]

for n in numbers:
    print(f"Number {n}: ", reverse(n))