a, m, d, n = map(int, input().split()) #시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)
count = 1 #몇 번 반복했는지 나타내는 변수

while count<n :
  a = (a*m)+d
  count += 1 #반복문 한 번 수행할 때마다 +1

print(a)