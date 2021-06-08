#9	2941	크로아티아 알파벳
#크로아티아 알파벳의 개수를 세는 문제

#첫 번째 안 보고 작성
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] #변경해서 입력된 크로아티아 알파벳
alphabet = input() #알파벳 입력

for i in croatia :
  alphabet = alphabet.replace(i, 'a')

print(len(alphabet))



'''
#첫 번째 베껴쓰기
alphabet = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croatia :
  alphabet = alphabet.replace(i, 'c')
print(len(alphabet))



#첫 번째 시도
croatia = list(input())
change = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
num = 0
i = 0

while croatia[i] != croatia[-3] :
  for j in range(len(change)) :
    if croatia[i:i+2] == change[j] :
      num += 1
      i += 2
  if croatia[i:i+3] == 'dz=' :
    num += 1
    i += 3
  else :
    num += 1
    i += 1

print(num) #크로아티아 알파벳 몇 개인지 출력
'''