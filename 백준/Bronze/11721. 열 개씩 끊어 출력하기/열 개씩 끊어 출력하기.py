import sys

word = sys.stdin.readline().rstrip()
cnt = len(word) // 10
for i in range(cnt+1):
  print(word[i*10:(i+1)*10])