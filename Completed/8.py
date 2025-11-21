def myAtoi(s: str) -> int:
    # Whitespace
    s = s.strip()

    # If the string is empty, return 0
    if not s: 
        return 0
    
    # Signedness
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # Conversion
    result = 0
    for char in s:
        if not char.isdigit():
            break
            
        result = result * 10 + int(char)

    result *= sign

    # Rounding
    if result < -2**31:
        return -2**31
    elif result > 2**31 - 1:
        return 2**31 - 1
    else:
        return result
    
    

numbers = ["42", "   -42", "4193 with words", "words and 987"]

for number in numbers:
    print(f"Number: {number} is: ", myAtoi(number))