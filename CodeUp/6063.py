a, b = input().split()
a = int(a) #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b) #변수 b의 값을 정수로 바꾸어 변수 b에 저장
c = (a if (a>=b) else b) #변수 c는 3항 연산으로 a가 b 이상일 경우 a값 출력, b가 a 초과일 경우 b값 출력
print(int(c))
print(c)

#print()에서 c를 정수로 바꾸어 출력한 이유는?

'''
3개의 요소로 이루어지는 3항 연산은
"x if C else y"의 형태로 작성됨
- C : True 또는 False 를 평가할 조건식 또는 값
- x : C의 평가 결과가 True 일 때 사용할 값
- y : C의 평가 결과가 True 가 아닐 때 사용할 값

조건식 또는 값이 True면 x값, Flase면 y값 사용
'''