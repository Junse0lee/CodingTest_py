#인덱스 번호 추출 
#인덱스 번호에 맞는 arr 추출
#sort로 정렬 후 -> 해당 k값보다 큰 경우 그 값을 result.append 진행 후 break

def solution(arr, queries):
    result = []
    abstract_arr= []
    for s, e, k in queries:
        abstract_arr = arr[s:e+1]
        abstract_arr.sort()
        for i in range(len(abstract_arr)):
            if abstract_arr[i] > k:
                result.append(abstract_arr[i])
                break
            elif i == len(abstract_arr)-1:
                result.append(-1)
    return result