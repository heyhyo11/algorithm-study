import sys

input = sys.stdin.readline

y1, m1, d1 = input().split() # 생년월일
y2, m2, d2 = input().split() # 기준 날짜

if int(m1) < 10: m1 = '0' + m1
if int(m2) < 10: m2 = '0' + m2
if int(d1) < 10: d1 = '0' + d1
if int(d2) < 10: d2 = '0' + d2

age1 = int(y1+m1+d1)
age2 = int(y2+m2+d2)

man_age = (age2-age1) // 10000
count_age = int(y2)-int(y1)+1
year_age = int(y2)-int(y1)

print(man_age, count_age, year_age, sep='\n')