def replace_pi(char):
    if len(char) == 0 or len(char) == 1:
        return char

    if char[0] == 'p' and char[1] == 'i':
        smalleroutput = replace_pi(char[2:])
        return '3.14' + smalleroutput
    else:
        smalleroutput = replace_pi(char[1:])
        return char[0] + smalleroutput


print(replace_pi('abcpippi'))
