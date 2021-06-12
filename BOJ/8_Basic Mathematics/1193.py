# 3	1193	분수찾기
# 분수의 순서에서 규칙을 찾는 문제

# 종이에 적어보아도 규칙을 알아내기 어려워 https://deokkk9.tistory.com/11의 코드와 해설을 보고 작성했습니다.

x = int(input())

line = 1

while x>line :
  x-=line
  line+=1
  
if line%2==0 :
  a=x
  b=line-x+1
else :
  a=line-x+1
  b=x

print(a, '/', b, sep='')



# # 코드 안 보고 작성
# x = int(input())

# line = 1

# while x>line :
#   x-=line
#   line+=1
  
# if line%2==0 :
#   a=x
#   b=line-x+1
# else :
#   a=line-x+1
#   b=x

# print(a, '/', b, sep='')