#A+B - 5
#if문 작성안하고 컴파일 오류나서 어렵게 생각해서 오래걸림 (예제 입력이 한 번에 이루어 진다고 생각함))

while True :
  a, b = map(int, input().split())
  if a==0 and b==0 :
    break
  print(a+b)