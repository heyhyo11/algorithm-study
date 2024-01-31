# 참고 블로그: https://sujeng97.tistory.com/12

n = int(input())

def star(l):
    if l == 3:
        return ['  *  ',' * * ','*****']

    arr = star(l//2)
    stars = []
    # 제일 상단의 삼각형 1개: n번째 줄의 절반만큼 양 옆에 공백이 있음
    for i in arr:
        stars.append(' '*(l//2)+i+' '*(l//2))

    # 양 옆의 삼각형 2개: stars에 이미 공백을 포함해서 들어간 상태임
    for i in arr:
        stars.append(i + ' ' + i)

    return stars

print('\n'.join(star(n)))