f = open('text2.txt','r')
f1= f.read()
f.close()

f1= f1.replace('java','python')

f = open('text2.txt','w')
f.write(f1)
f.close()