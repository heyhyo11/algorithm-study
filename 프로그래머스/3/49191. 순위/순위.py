# 풀이 참고

def solution(n, results):
    answer = 0
    graph = [[-1] * (n + 1) for _ in range(n + 1)]

    # 자기 자신과의 승부는 -1로 설정
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            if a == b :
                graph[a][b] = -1 
    
    # 1: 이긴 경우, 0: 진 경우
    for i, j in results :
        graph[i][j] = 1
        graph[j][i] = 0 

    # 플로이드-워셜 사용
    for k in range(1, n + 1) :
        for a in range(1, n + 1) :
            for b in range(1, n + 1) :
                if graph[a][k] == graph[k][b] == 1 :
                    graph[a][b] = 1
                    graph[b][a] = graph[k][a] = graph[b][k] = 0
    
    # 정답 확인
    for a in range(1, n + 1) :
        test_graph = graph[a][1 :]
        if test_graph.count(-1) == 1  :
            answer += 1

    return answer