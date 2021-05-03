n = int(input())

#조건/선택 실행구조 안에 다시 조건/선택 실행구조를 "중첩"할 수가 있다.
if n<0 : #변수 n이 음수일 경우 True
  if n%2==0 : #변수 n이 짝수일 경우 True
    print('A') #주의 : 변수 A와 문자열 'A'/ "A"는 의미가 완전히 다르다.
  else :
    print('B')
else :
  if n%2==0 :
    print('C')
  else :
    print('D')
