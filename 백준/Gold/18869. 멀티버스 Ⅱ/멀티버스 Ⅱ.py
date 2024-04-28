import sys

input = sys.stdin.readline

m, n = map(int, input().split()) # m: 우주 개수, n: 행성 개수
dict = {}

for _ in range(m):
    planets = list(map(int, input().split())) # 행성 입력
    sorted_planet = sorted(list(set(planets))) # 행성 중복 제거하고 오름차순 정렬
    rank = {sorted_planet[i]: i for i in range(len(sorted_planet))} # 행성 순위 매기기
    add = str([rank[planet] for planet in planets])
    dict[add] = dict.get(add, 0) + 1

print(sum(map(lambda x:x*(x-1)//2, dict.values())))
