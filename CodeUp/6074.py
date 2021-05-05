c = ord(input()) #입력한 알파벳 문자의 정수값을 변수 c에 저장
t = ord('a') #알파벳 문자 a의 정수값을 변수 t에 저장
while t<=c :
  print(chr(t), end=' ') #값 출력 후 마지막(end)에 빈칸, end='\n'이면 줄바꿈
  t += 1