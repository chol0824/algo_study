import sys
from collections import deque

inp = sys.stdin.readline

n = int(inp())
cnt = 0
q = deque()

for i in range(n):
  top = int(inp())
  while q and q[-1] <= top:
    q.pop()
  cnt += len(q)
  q.append(top)

print(cnt)
