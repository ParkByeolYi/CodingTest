a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(c and (not d) or ((not c) and d)) #XOR 연산 두 값의 True / False 값이 서로 다를 경우만 True 출력, 그 외의 경우에는 False 출력

#프로그래밍언어에서는 소괄호 () 만 사용