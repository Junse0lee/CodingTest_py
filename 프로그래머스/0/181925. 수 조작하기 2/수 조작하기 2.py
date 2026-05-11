#이 문제에서는 변화량이 가장 중요함 
#변화량을 가지고 푸는 문제라고 이해해도 됨

def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        value_num = numLog[i+1] - numLog[i]
        if value_num == 1:
            answer += "w"
        elif value_num == -1:
            answer += "s"
        elif value_num == 10:
            answer += "d"
        elif value_num == -10:
            answer += "a"
        
    return answer