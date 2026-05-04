import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K and len(scoville) >=2:
        smallest0 = heapq.heappop(scoville)
        smallest1 = heapq.heappop(scoville)
        new_scoville = smallest0 + 2*smallest1 
        heapq.heappush(scoville, new_scoville)
        count += 1
        
    if scoville[0] >= K:
        return count
    else:
        return -1
    