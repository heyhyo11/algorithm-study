import sys

N = int(sys.stdin.readline().rstrip())

box_5kg = -1
box_3kg = -1

18
try:
  for i in range(0, N+1, 3):
    for j in range(0, N+1, 5):
      if (i + j) == N:
        box_3kg = (i//3)
        box_5kg = (j//5)
        raise NotImplementedError
except:
  pass

if box_5kg == -1 and box_3kg == -1:
  print(-1)
else:
  print(box_5kg + box_3kg)