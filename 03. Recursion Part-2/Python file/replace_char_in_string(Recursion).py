def replace_char(char, a, b):
    if len(char) == 0:
        return char

    smalleroutput = replace_char(char[1:], a, b)
    if char[0] == a:
        return b + smalleroutput
    else:
        return char[0] + smalleroutput


char = 'xxyy'
print(replace_char(char, 'x', 'y'))