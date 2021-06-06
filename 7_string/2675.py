#4	2675	문자열 반복
#각 문자를 반복하여 출력하는 문제

t = int(input())

for i in range(t) :
  n, s = input().split()
  n = int(n)
  s = list(s)
  output = ''

  for j in range(len(s)) :
    for k in range(n) :
      output += s[j]
      
  print(output)