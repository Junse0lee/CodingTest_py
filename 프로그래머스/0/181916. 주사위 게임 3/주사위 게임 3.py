def solution(a, b, c, d):
    set_list = set([a,b,c,d])
    dice_list = [a,b,c,d]
    if len(set_list) == 1:
        set_list = list(set_list)
        return 1111 * set_list[0]
    else:
        for i in set_list:
            if dice_list.count(i) == 2:
                if len(set_list) == 2: #두개씩 같은 값이 있을 때
                    set_list = list(set_list)
                    return (set_list[0] + set_list[1]) * abs(set_list[0] - set_list[1])
                else: #a,a,b,c
                    set_list.remove(i)
                    set_list = list(set_list)
                    return set_list[0] * set_list[1]
            elif dice_list.count(i) == 3:
                set_list.remove(i)
                set_list = list(set_list)
                return (10*i+set_list[0])**2
        return min(dice_list)
    
            
            
    
    
    