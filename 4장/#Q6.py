user_input = input('입력할 내용 : ')

f = open('text1.txt','a') # 내용 추가를 위해 'a'
f.write(user_input) # 입력한 내용 쓰기
f.write('\n') # 줄 바꾸기
f.close()