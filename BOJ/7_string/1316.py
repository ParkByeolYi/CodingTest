#10	1316	그룹 단어 체커
#조건에 맞는 문자열을 찾는 문제

n = int(input())
output = n

for i in range(n) :
  word = list(input())
  unique_word = []

  for j in range(len(word)) :
    #아닐 경우로 작성했어야 하는데 '=='로 적어서 오류, 구글링 후 '!='로 바꿈
    if j != len(word)-1 :
      if word[j] == word[j+1] :
        continue
    #unique_word 리스트에 있는지 확인
    if word[j] in unique_word :
      output -= 1
      break
    else :
      unique_word.append(word[j])

print(output)