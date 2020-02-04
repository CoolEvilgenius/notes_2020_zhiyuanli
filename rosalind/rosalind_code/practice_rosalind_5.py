# 代码
import os
os.chdir("C:\\Users\\Administrator\\Desktop\\python_operation")
os.getcwd()
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


def countGC(list):
    """计算GC含量的函数"""

    numGC = list.count('G') + list.count('C')

    perGC = float(numGC) / len(list)
    return perGC * 100


f = open('rosalind_gc.txt', 'r')

lines = f.readlines()

f.close()

(index, seq) = readfasta(lines)  # 接收序列名和序列

result = []

for i in seq:
    result.append(countGC(i))

maxID = index[result.index(max(result))].replace('>', "").replace("\n", "")

seqGC = max(result)

print(maxID)

print(round(seqGC, 6))
