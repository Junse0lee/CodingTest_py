def solution(code):
    
    mode = 0
    answer = ''
    for i in range (len(code)):
        if mode == 0:
            if code[i] != "1":
                if i % 2 == 0:
                    answer += code[i]
            else:
                mode = 1
                
        elif mode == 1:
            if code[i] != "1":
                if i % 2 == 1:
                    answer += code[i]
            else:
                mode = 0
                
    if answer == '':
        return "EMPTY"
    else:
        return answer