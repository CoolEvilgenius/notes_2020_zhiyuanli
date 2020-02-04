import os
os.chdir("C:\\Users\\Administrator\\Desktop\\python_operation")

seq = open('rosalind_9.txt','r')
seq_all = seq.readlines()
seq_1 = seq_all[0].strip()
seq_2 = seq_all[1].strip()

i = 0

while i < len(seq_1)-len(seq_2):

    if (seq_1[i:i + len(seq_2)]) == seq_2:
        print(i + 1)
    i = i + 1






