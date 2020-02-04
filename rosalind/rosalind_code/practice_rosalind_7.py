k = 22
m = 28
n = 24
s = k + m + n
c = 1 - (n/s * (n-1)/(s-1) + 2 * n/s * 0.5 * m/(s-1) + m/s * (m-1)/(s-1) * 0.25)
print(round(c,5))
