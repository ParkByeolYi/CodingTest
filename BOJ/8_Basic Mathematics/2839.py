# 7	2839	설탕 배달
# 5와 3을 최소 횟수로 합하여 N을 만드는 문제

'''
n = int(input())
result = 0

five = n//5
result += five
n = n-five*5

if n%3 == 0 :
  while n >= 3 :
    result += 1
    n -= 3
  print(result)
else :
  print(-1)
'''

# 코드 리뷰
# 예제 1, 2는 동작되나 3, 4, 5 실행 시에 -1이 출력된다. 3과 5의 조합으로 -1이 출력되지 않도록 해야하는 문제인데 모르겠다.



# https://ooyoung.tistory.com/81
# 처음부터 5를 빼지 말고 5의 배수가 될 경우 if문으로 들어가면되는 쉬운 문제였다. 파이썬에서 while ~ else 반복문 사용이 가능한 것을 처음 알았다.
# 코드 안 보고 다시 작성
sugar = int(input())
bag = 0

while sugar >= 0: 
  if sugar % 5 == 0 : # 5의 배수이거나 설탕이 0이 되면 조건문 성립하여 3의 배수로만 있어도 print(bag) 실행됨
    bag += int(sugar/5) # 5로 나눈 몫을 구해야 정수가 됨
    print(bag)
    break
  sugar -= 3
  bag += 1 # 5의 배수가 될 때까지 설탕 -3, 봉지 +1
else :
  print(-1) 
