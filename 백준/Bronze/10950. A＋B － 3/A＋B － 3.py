chance = int(input())
sum_list = []


for i in range(chance):
  num = list(map(int, input().split()))
  num_sum = sum(num)
  sum_list.append(num_sum)
  
for i in range(chance):
  print(sum_list[i])