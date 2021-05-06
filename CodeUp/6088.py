#등차(차이가 같다) 수열
a, d, n = map(int, input().split()) #시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)
count = 1

while count<n :
  a += d
  count += 1

print(a)