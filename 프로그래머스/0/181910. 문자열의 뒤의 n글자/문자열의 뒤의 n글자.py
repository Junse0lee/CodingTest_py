def solution(my_string, n):
    # 14에서 11을 빼면 3 -> 0~2까지를 제외하면 result
    # 10에서 5를 빼면 5 -> 0~4까지를 제외하면  result
    string_name_index = len(my_string) - n
    string_name = my_string[string_name_index: ]
    
    return "".join(string_name)