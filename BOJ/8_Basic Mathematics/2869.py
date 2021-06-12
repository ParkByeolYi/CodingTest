# 4	2869	달팽이는 올라가고 싶다
# 달팽이의 움직임을 계산하는 문제

'''
a, b, v = map(int, input().split())
meter = a
day = 1

for i in range(v) :
  if a == v :
    print(1)
  else :
    meter += a-b
    day += 1
    if meter >= v :
      print(day)
      break
'''



# 코드 리뷰
# 문제를 보면서 for문이나 while문같은 반복문을 사용하면 시간 초과될 것이라고 알았으나 반복문 사용없이 코드가 생각이 안났다. 그래서
# https://stultus.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-2869-%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4 참고하여 다시 공부했다. 

a, b, v = map(int, input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1) # 삼항연산자