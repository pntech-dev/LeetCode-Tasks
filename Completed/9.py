def isPalindrome(x: int) -> bool:
    return True if str(x) == str(x)[::-1] else False


numbers = [121, -121, 10, 8, 0, 123]

for n in numbers:
    print(f"Number {n}: ", isPalindrome(n))