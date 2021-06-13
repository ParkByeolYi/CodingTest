# 5	10250	ACM 호텔
# 호텔 방 번호의 규칙을 찾아 출력하는 문제

t = int(input())

for _ in range(t) :
  h, w, n = list(map(int, input().split())) #호텔의 층 수, 각 층의 방 수, 몇 번째 손님

  if n%h == 0 :
    first = h
    second = int(n/h)
        
  else :
    first = n%h
    second = int(n/h+1)
  
  if second < 10 :
    print(first, '0', second, sep='')
  elif second >= 10 :
    print(first, second, sep='')

# 코드 리뷰
# 분명 맞는 것 같은데 계속 틀렸다고 나와서 구글링으로 알아보니 조건문을 'if n%h == 0 or h == n or w == n :'로 작성했기 때문이었다. 'h==n'은 'n%h==0'과 똑같은 것이고 'w==n'는 경우의 수를 계산하는 과정에서 틀렸다.
# 또한, 출력문을 10이상, 미만으로 나누지 말고 층에 100을 곱하면 된다. ex) print(first*100+second)
