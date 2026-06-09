def solution(my_string, queries):
    my_string = list(my_string)
    for i,j in queries:
        new_list = my_string[i:j+1]
        new_list.reverse()
        my_string[i:j+1] = new_list
    return ''.join(my_string)