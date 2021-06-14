# 6	2775	부녀회장이 될테야
# 층과 거주자 수의 규칙을 찾는 문제

t = int(input())
for _ in range(t) :
  k = int(input()) # k층
  n = int(input()) # n호

  people = 1

  if k == 1 :
    for i in range(2, n+1) :
      people += i
      print(people)

  elif n == 1 :
    people = 1

  elif k != 1 or n != 1 :
    for _ in range(2, n+1) :
      people += people
      print(people)

  print(people)
