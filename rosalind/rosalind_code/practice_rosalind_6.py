import os
os.chdir("C:\\Users\\Administrator\\Desktop\\python_operation")
os.getcwd()
f = open('rosalind_hamm.txt','r')

lines = f.readlines()

f.close()

s1 = lines[0].strip()

s2 = lines[1].strip()

hd = 0

for i in range(len(s1)):

    if s1[i] != s2[i]:

        hd  += 1

print(hd)