n1, n2 = input().split()
c = float(n1) + float(n2) #숫자로 구성된 문자열이나 정수를 실수 값으로 바꾸기 위해 float()를 사용하였다. (소수점은 위치가 정해져있지 않고 이리저리 둥둥 떠다니므로, floating point라고 부른다.)
print(c)

#6026.py 코드에서 입력값을 마이너스 실수(-) 공백(' ') 실수(+) 값을 입력하면 0.xxxx00000053등으로 출력되는데 이유는?
#부동소수점 오차? 컴퓨터가 사용하는 이진법체계에서 십진법 소수를 완전하게 표현할 수 없기 때문이다. https://python.flowdas.com/tutorial/floatingpoint.html 공부 필요.