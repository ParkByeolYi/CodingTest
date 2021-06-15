# 6	2775	부녀회장이 될테야
# 층과 거주자 수의 규칙을 찾는 문제

# 처음 생각한 답안
'''
t = int(input())
for _ in range(t) :
  k = int(input()) # k층
  n = int(input()) # n호

  people = 1
  down = 0

  if k == 1 :
    for _ in range(n-1) :
      people += 1
      print(1, people)

  else :
    for i in range(2, n) :
      down += i
    
    people += down
    print(3, people)

  print('final', people)
'''

# 코드 리뷰
# 30분 이상 생각해봐도 풀이 방법이 안 떠올라서 답안을 검색했다. 3중 for문을 작성하면 되는 문제였는데.. 분명 시작할 때 시간 제한이 넉넉해서 2중 for문을 하면 되겠다고만 생각했었다.



# https://ooyoung.tistory.com/89 코드 베껴쓰기
'''
t = int(input())

for _ in range(t) :
  floor = int(input())
  num = int(input())
  f0 = [x for x in range(1, num+1)]

  for k in range(floor) :
    for i in range(1, num) :
      f0[i] += f0[i-1]
    print(f0) # 프린트문 추가
  
  print(f0[-1])
'''

#코드 안 보고 작성
t = int(input())

for _ in range(t) :
  floor = int(input())
  num = int(input())
  f0 = [x for x in range(1, num+1)]

  for k in range(floor) :
    for i in range(1, num) :
      f0[i] += f0[i-1]

  print(f0[-1])
