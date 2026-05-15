n = int(input("Nhập số nguyên dương n: "))

s = str(n)
length = len(s)

S = 0
so_con_list = []

for i in range(length):
    for j in range(i + 1, length + 1):
        sub = int(s[i:j])
        so_con_list.append(sub)
        S += sub ** 2

print("Các số con:", so_con_list)
print("S =", S)