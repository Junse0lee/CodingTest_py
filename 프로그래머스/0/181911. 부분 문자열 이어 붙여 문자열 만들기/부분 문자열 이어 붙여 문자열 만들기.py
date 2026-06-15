def solution(my_strings, parts):
    answer= ""
    i = 0
    for string_content in my_strings:
        k, j = parts[i]    
        answer += "".join(string_content[k :j+1: 1])
        i +=1
            
    return answer