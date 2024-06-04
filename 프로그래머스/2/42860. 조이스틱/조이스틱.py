def solution(name):
    ans = 0
    min_move = len(name) - 1
    next = 0
    
    # 예외처리: 제일 마지막에 'A'로 끝나는 경우
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1
    
    # 예외처리: name = 'A' 이었던 경우 바로 리턴
    if (min_move < 0):
        return answer
        
    for i, char in enumerate(name):
        # 상하 이동
        ans += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 좌우 이동
        next = i + 1 # A가 나오는 마지막 인덱스
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # (1) 왼쪽 -> 오른쪽, (2) 왔다 갔다 중에서 최솟값
        min_move = min(min_move, 2*i+len(name)-next, i+2*(len(name)-next))
    ans += min_move
    return ans