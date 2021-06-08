#5	1157	단어 공부
#주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

#처음 문제를 읽고 대문자, 소문자를 넣어둔 리스트와 비교해서 숫자를 증가시킨 다음 대소문자 합친 결과값 중에 가장 큰 값을 출력하려 했는데 연속 알파벳 문제가 나오니 알파벳 불러오는 방법이 있는지 궁금해 먼저 풀이를 봄

#첫 번째 안보고 작성
words = input().upper()
unique_words = list(set(words)) #중복 제거

cnt_list = []
for i in unique_words :
  cnt = words[i]
  cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
  print('?')
else :
  max_index = cnt_list.index(max(cnt_list))
  print(unique_words[max_index])


'''
#두 번째 베껴쓰기
words = input().upper()
unique_words = list(set(words)) #unique_words의 값은 순서에 상관없이 저장됨

cnt_list = []
for i in unique_words :
  cnt = words.count[i]
  cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
  print('?')
else :
  max_index = cnt_list.index(max(cnt_list))
  print(unique_words[max_index])



#첫 번째 베껴쓰기
#https://ooyoung.tistory.com/70
words = input().upper() #입력받으면서 대문자로 바꿈
unique_words = list(set(words)) #입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
  cnt = words.count(x)
  cnt_list.append(cnt) #count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 : #count 숫자 최대값이 중복되면
  print('?')
else :
  max_index = cnt_list.index(max(cnt_list)) #count 숫자 최대값 인덱스(위치)
  print(unique_words[max_index])
'''