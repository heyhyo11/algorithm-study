import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    min_sum = 0
    cnt = 0
    
    while scoville[0] < K:
        try:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2*2)
            cnt += 1
        except:
            return -1
    return cnt