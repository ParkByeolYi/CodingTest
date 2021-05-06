n = int(input(), 16) #입력된 값을 16진수로 인식해 변수 n에 저장
for i in range(1, int('F', 16)+1) : #1부터 16진수 'F'까지
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')