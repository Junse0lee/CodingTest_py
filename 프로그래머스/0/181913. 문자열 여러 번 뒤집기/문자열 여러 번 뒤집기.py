def solution(my_string, queries):
    array_list = list(my_string)
    for i,j in queries:
        array_list[i:j+1] = array_list[i:j+1][::-1]
    return ''.join(array_list)