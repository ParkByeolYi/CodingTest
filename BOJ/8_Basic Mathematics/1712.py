# 1	1712	손익분기점
# 이익이 발생하는 지점을 찾는 문제

'''
a, b, c = map(int, input().split())
i = 0

while True :
  if b >= c :
    print('-1')
    break

  i += 1
  cost = a+b*i # 총 비용(=고정비용+가변비용)
  income = c*i # 총 수입
  
  if cost < income :
    print(i)
    break
'''

# 코드 리뷰
# b>=c인 조건문까지 생각을 잘 했으나 예제 3에서 시간 초과가 계속 발생하여 답안을 찾아보니 while문을 이용했기 때문이었다. 문제를 풀 때 간단하게 나타낼 수 있는 수식이 있는지 생각하는 습관을 들여야겠다.



#https://deokkk9.tistory.com/3를 보고 이해하여 안 보고 다시 작성

a, b, c = map(int, input().split())
if b>=c : print('-1')
else : print(int(a/(c-b)+1))