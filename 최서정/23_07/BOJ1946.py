import sys

inp = sys.stdin.readline

t = int(inp())
for _ in range(t):
  n = int(inp())
  grade = []
  cnt = 1
  for _ in range(n):
    first, second = map(int,inp().split())
    grade.append((first,second))
  grade.sort()
  last = grade[0][1]
  for i in range(1,n):
    if grade[i][1] == 1:
      cnt+=1
      break
    if last > grade[i][1]:
      cnt+=1
      last = grade[i][1]
  print(cnt)
