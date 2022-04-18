list1 = list(map(int, input().split()))
new_list = {}


for i in list1:
  try: new_list[i] += 1
  except: new_list[i] = 1
  
# print('list1: ', list1)
# print('new_list: ', new_list)

x = [k for k, v in new_list.items() if max(new_list.values()) == v]

# print(x[0])
# print(new_list[x[0]])

if (new_list[x[0]] == 3):
  prize = 10000 + x[0] * 1000
  print(prize)
elif (new_list[x[0]] == 2):
  prize = 1000 + x[0] * 100
  print(prize)
else:
  number = max(x)
  prize = 100 * number
  print(prize)