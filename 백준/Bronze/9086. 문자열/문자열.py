import sys

t = int(sys.stdin.readline())
for _ in range(t):
  word = sys.stdin.readline().rstrip()
  if len(word) == 1:
    word += word[-1]
  print(word[0]+word[-1])