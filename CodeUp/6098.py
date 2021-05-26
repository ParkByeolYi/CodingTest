d = []
for i in range(10) :
  d.append([])
  for j in range(10) :
    d[i].append(0)

'''
for i in range(10) :
  for j in range(10) :
    d[i][j] = input().split()
'''

for i in range(9) :
  a = input().split()
  for j in range(9) :
    d[i+1][j+1] = int(a[j])

d[1][1] == 9
i = int(1)
j = int(1)

while True :
  if d[i+1][j] == 0 :
    i += 1
    d[i][j] = 9
  elif d[i+1][j] == 1 :
    j += 1
    d[i][j] = 9
  elif d[i+1][j] == 2 :
    i += 1
    d[i][j] = 9
    break
  elif d[i][j+1] == 2 :
    j += 1
    d[i][j] = 9
    break

for i in range(10) :
  for j in range(10) : 
    print(d[i][j], end=' ')
  print()