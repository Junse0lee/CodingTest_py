def solution(arr, queries):
    for k in range (len(queries)):
        i, j = queries[k]
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp 
    return arr
    
            
        