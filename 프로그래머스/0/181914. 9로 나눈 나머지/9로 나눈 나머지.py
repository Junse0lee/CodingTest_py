def solution(number):
    num_list = list(number)
    sum_list = 0
    for num in num_list:
        sum_list = sum_list + int(num)
    return (sum_list % 9)