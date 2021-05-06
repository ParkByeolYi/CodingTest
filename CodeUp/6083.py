r, g, b = map(int, input().split())
sum = 0

for i in range(r) :
  for j in range(g) :
    for k in range(b) :
      print(i, j, k)
      sum += 1

print(sum)

#3중 중첩 반복문을 실제 프로젝트에서 사용해도 되는걸까?