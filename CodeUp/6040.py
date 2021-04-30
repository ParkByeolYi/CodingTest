a, b = input().split()
n = int(a)//int(b) #나눈 몫을 계산하는 연산자(//) a를 b로 나눈 몫을 계산해 줌
print(n)

'''
<인터넷 검색>
문제 참고의 print(a//b)를 사용해보고 싶기 때문
map() 내장함수를 사용하여
a, b = map(int, input().split())
print(a//b)
'''