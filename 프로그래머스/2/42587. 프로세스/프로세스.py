from collections import deque

def solution(priorities, location):
    count = 0
    que = deque([(p, i) for i, p in enumerate(priorities)])
    while que:
        priority, index = que.popleft()
        
        if any(priority < q[0] for q in que):
            que.append((priority, index))
        else:
            count +=1
            
            if index == location:
                return count