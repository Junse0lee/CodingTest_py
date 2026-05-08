def solution(num_list):
    num_sum = 0
    multiply = 1
    for i in range(len(num_list)):
        num_sum +=num_list[i]
        multiply *= num_list[i]
    
    if num_sum **2 > multiply:
        return 1
    else:
        return 0
    
