#등비(비율이 같다) 수열
a, r, n = map(int, input().split()) #시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)
count = 1

while count<n :
  a *= r
  count += 1

print(a)