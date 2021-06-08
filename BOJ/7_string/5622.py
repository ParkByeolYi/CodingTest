#8	5622	다이얼
#규칙에 따라 문자에 대응하는 수를 출력하는 문제

num = list(input())
time = 0

for i in num :
  if i == 'A' or i == 'B' or i == 'C' :
    time += 3 #숫자 1을 걸려면 총 2초가 필요하기 때문에 한 칸 옆에 있는 숫자인 2를 걸려면 +1을 하여 3초
  elif i == 'D' or i == 'E' or i == 'F' :
    time += 4
  elif i == 'G' or i == 'H' or i == 'I' :
    time += 5
  elif i == 'J' or i == 'K' or i == 'L' :
    time += 6
  elif i == 'M' or i == 'N' or i == 'O' :
    time += 7
  elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
    time += 8
  elif i == 'T' or i == 'U' or i == 'V' :
    time += 9
  elif i == 'W' or i == 'X' or i == 'Y'or i == 'Z':
    time += 10

print(time)