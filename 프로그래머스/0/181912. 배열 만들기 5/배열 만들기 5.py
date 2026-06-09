def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        num = list(num)
        num_int= ''.join(num[s:s+l])
        num_int = int(num_int)
        if num_int > k:
            answer.append (num_int)
            
    return answer