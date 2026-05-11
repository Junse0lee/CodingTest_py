#배열 만들기-> 
#각 str에 0을 더하거나 5를 더하고 이를 숫자로 변환한 다음 l와 r과 비교했을 때 l보다 크고 r보다 작으면 대입 이런 식?
def solution(l, r):
    result = []
    number = ["0", "5"]
    
    for i in range(l, r+1):
        target_num = str(i)
        boolienType = True
        for j in target_num:
            if j not in number:
                boolienType = False
                break
        if boolienType ==True:
            result.append(i)
            
    if result:
        return result
    else:
        return [-1]
        
    