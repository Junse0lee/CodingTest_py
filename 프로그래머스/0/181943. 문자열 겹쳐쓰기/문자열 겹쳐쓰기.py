def solution(my_string, overwrite_string, s):
    a = len(overwrite_string)
    b = my_string[s:s+a]
    b2 = my_string[s+a: ]
    b1 = my_string[:s]
    b3 = b.replace(b, overwrite_string)
    answer = b1+b3 + b2
    return answer