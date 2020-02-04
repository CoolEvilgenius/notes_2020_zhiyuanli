import os
os.chdir("C:\\Users\\Administrator\\Desktop\\python_operation")


def readfasta(lines):
    """读入并处理FASTA文件的函数"""

    seq = []

    index = []

    seqplast = ""

    numlines = 0

    for i in lines:

        if '>' in i:  # 判断是序列行还是说明行
            index.append(i.replace("\n", "").replace(">", ""))
            seq.append(seqplast.replace("\n", ""))
            seqplast = ""
            numlines += 1
        else:
            seqplast = seqplast + i.replace("\n", "")  # 把分行的序列拼接成一个字符串
            numlines += 1
        if numlines == len(lines):
            seq.append(seqplast.replace("\n", ""))
    seq = seq[1:]
    return index, seq

f = open('rosalind_10_cons.txt', 'r')
lines = f.readlines()
f.close()
(index, seq) = readfasta(lines)

A = []
G = []
T = []
C = []
i = 0

while i < len(seq[0]):
    j = 0
    num_a = 0
    num_g = 0
    num_t = 0
    num_c = 0
    while j < len(seq):
        if seq[j][i] == 'A':
            num_a += 1
        elif seq[j][i] == 'G':
            num_g += 1
        elif seq[j][i] == 'T':
            num_t += 1
        elif seq[j][i] == 'C':
            num_c += 1
        j += 1
    i += 1
    A.append(num_a)  # 记录该位点出现”A”的次数
    G.append(num_g)
    C.append(num_c)
    T.append(num_t)

common = ''
base = 0
while base < len(A):
    if max(A[base], G[base], C[base], T[base]) == A[base]:
        common += 'A'
    elif max(A[base], G[base], C[base], T[base]) == G[base]:
        common += 'G'
    elif max(A[base], G[base], C[base], T[base]) == T[base]:
        common += 'T'
    elif max(A[base], G[base], C[base], T[base]) == C[base]:
        common += 'C'
    base += 1

    # 把计数各项从整数改为字符串型，方便写入输出文件
i = 0
while i < len(A):
    A[i] = str(A[i])

    G[i] = str(G[i])

    C[i] = str(C[i])

    T[i] = str(T[i])
    i += 1


f = open('practice_rosalind_10_output.txt','a')
f.write(common + '\n')
f.write("A: ")
f.write(' '.join(A) + '\n')
f.write("C: ")
f.write(' '.join(C) + '\n')
f.write("G: ")
f.write(' '.join(G) + '\n')
f.write("T: ")
f.write(' '.join(T))
f.close()





