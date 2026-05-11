#아이디어: 배열로 바꿔서 순회 -> n번
#아이디어: enumerate로 바꿔서 해당 값의 개수에 따라서 덧셈, 뺄셈을 해도 괜찮지 않을까? => 곱셈이 없으니까 n번보다 작을 것 같은데 

def solution(n, control):
    control_list = list(control)
    w_word_count = control_list.count("w")
    s_word_count = control_list.count("s")
    d_word_count = control_list.count("d")
    a_word_count = control_list.count("a")
    
    answer = n + (w_word_count * 1) + (s_word_count * -1) + (d_word_count * 10) + (a_word_count * -10)
    return answer