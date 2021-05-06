a, b, c = map(int, input().split()) #3명의 사람의 방문 주기
d = 1 #day로 날 수

while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1

print(d) #3명이 다시 모두 함께 방문해 문제를 풀어보는 날