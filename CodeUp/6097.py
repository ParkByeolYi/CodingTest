#기본 격자판 생성
h, w = map(int, input().split())
a = []
for i in range(h) :
  a.append([])
  for j in range(w) :
    a[i].append(0)

n = int(input())
for i in range(n) : #n개의 막대
  l, d, x, y = map(int, input().split())
  for j in range(l) : #막대의 길이
    if d == 0 :
      a[x-1][y-1+j] = 1
    elif d == 1:
      a[x-1+j][y-1] = 1

for i in range(h) :
  for j in range(w) :
    print(a[i][j], end=' ')
  print()