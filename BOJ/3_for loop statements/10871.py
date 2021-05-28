#X보다 작은 수

n, x = map(int, input().split())

#a = list(map(int, input().split()))
a = map(int, input().split())
b = []

for i in a :
  if i < x :
    b.append(i)

for i in b :
  print(i, end=' ')