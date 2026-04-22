def solution(a, b):
    b2 = 2 * a* b
    a = str(a)
    b = str(b)
    
    answer = max(int(a+b), b2)
    return answer