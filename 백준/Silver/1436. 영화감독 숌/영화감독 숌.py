import sys

# 1. 리스트 만들기
num_list = []

for i in range(10000):
  num1 = str(i) + '666'
  if i < 10:
    num2 = '666' + '000' + str(i)
  elif i < 100:
    num2 = '666' + '00' + str(i)
  elif i < 1000:
    num2 = '666' + '0' + str(i)
  else:
    num2 = '666' + str(i)
  num_list.append(num1)
  num_list.append(num2)


for i in range(1000):
  for j in range(10):
    num1 = str(i) + '666' + str(j)
    if i < 10:
      num2 = str(j) + '666' + '00' + str(i)
    elif i < 100:
      num2 = str(j) + '666' + '0' + str(i)
    else:
      num2 = str(j) + '666' + str(i)
    num_list.append(num1)
    num_list.append(num2)


for i in range(100):
  for j in range(100):
    if j < 10:
      num1 = str(i) + '666' + '0' + str(j)
    else:
      num1 = str(i) + '666' + str(j)
    num_list.append(num1)


num_list = list(set(map(int, num_list)))
num_list.sort()


# 2. 입력 받기
N = int(sys.stdin.readline().rstrip())

# 3. 출력
print(num_list[N-1])