#3	10809	알파벳 찾기
#한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제

s = list(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
output = [-1 for i in range(26)] #파이썬 길이 26 및 -1로 초기화

for i in s :
  for j in range(26) :
    if i == alphabet[j] :
      if output[j] == -1 :
        output[j] = s.index(alphabet[j])
      break #if문을 실행했거나 중복되는 알파벳이 있으면 break로 for문 빠져나감

for i in range(26) :
  print(output[i], end=' ')