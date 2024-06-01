import sys
input = sys.stdin.readline

dna = ['A', 'C', 'G', 'T']
check_list = [0] * 4 # 비밀번호 체크리스트
my_list = [0] * 4 # 현재 상태 리스트
check_secret = 0 # 몇 개의 문자 조건을 만족했는지

# 새로 들어온 문자를 처리하는 함수
def myadd(c):
    global check_list, my_list, check_secret
    for i in range(len(dna)):
        if c == dna[i]: # 예) c == 'A'
            my_list[i] += 1 # 현재 상태 리스트 +=1
            if my_list[i] == check_list[i]: # 문자 조건을 만족했다면 +=1
                check_secret += 1

# 제거되는 문자를 처리하는 함수
def myremove(c):
    global check_list, my_list, check_secret
    for i in range(len(dna)):
        if c == dna[i]:
            if my_list[i] == check_list[i]:
                check_secret -= 1
            my_list[i] -= 1

# 입력 받기
s, p = map(int, input().split()) # s: 문자열 크기, p: 부분 문자열 크기
a = list(input()) # 문자열 데이터
check_list = list(map(int, input().split())) # 비밀번호 체크리스트
answer = 0 # 정답

# check_list 탐색하여 값이 0인 데이터 개수만큼 check_secret 값 증가
# 값이 0이라는 것은 비밀번호 개수 조건을 이미 만족했다는 의미
for i in range(4):
    if check_list[i] == 0:
        check_secret += 1

# 부분 문자열의 문자 조건 확인
for i in range(p):
    myadd(a[i])

# 문자 조건을 충족하면 정답 += 1
if check_secret == 4:
    answer += 1

# 슬라이딩 윈도우를 사용하여 다른 부분문자열의 문자 조건 확인
for i in range(p, s):
    j = i - p
    myadd(a[i])
    myremove(a[j])
    if check_secret == 4:
        answer += 1

print(answer)
