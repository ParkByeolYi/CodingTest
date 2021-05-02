a, b, c = map(int, input().split())
d = ((a if a<b else b) if ((a if a<b else b)<c) else c) #3항 연산을 중첩하여 여러 값들을 순서대로 비교해 a, b, c 의 값 중 가장 작은 값을 변수 d에 저장
print(d)