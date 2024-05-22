def solution(progresses, speeds):
    
    n = len(progresses)
    finish_days = []

    for i in range(n):
        remain = 100 - progresses[i]
        day = remain // speeds[i]
        if remain % speeds[i] != 0:
            day +=1
        finish_days.append(day)
    
    now = 0
    answer = []
    for i in range(1,n):
        if finish_days[i] > finish_days[now]:
            answer.append(i - now)
            now = i
    answer.append(n-now)
    return answer