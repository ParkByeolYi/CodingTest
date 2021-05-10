n = int(input())
k = input().split()

for i in range(n) : #string형 값이 저장된 변수 k를 int형으로 바꾸어 줌
  k[i] = int(k[i])

a = k[0]

for i in range(n) :
  if a > k[i] :
    a = k[i]

print(a)