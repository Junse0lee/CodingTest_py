#이 문제에서는 변화량이 가장 중요함 
#변화량을 가지고 푸는 문제라고 이해해도 됨

def solution(numLog):
    answer = ''
    joystick = dict(zip([1, -1, 10, -10], ["w", "s", "d", "a"]))
    for i in range(1, len(numLog)):
        answer += joystick[numLog[i] - numLog[i-1]]
        
    return answer