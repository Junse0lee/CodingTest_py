#마지막 원소 > 그전 원소 -> 마지막 원소 - 그전 원소 
#마지막 원소 < 그전 원소 -> 마지막 원소 *2 
# 각각의 조건별 추가
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    elif num_list[-1] <= num_list[-2]:
        num_list.append(num_list[-1] * 2)
        
    return num_list