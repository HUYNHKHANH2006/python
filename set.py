'''
4. Set
4.10. Thực hành
iii. Viết chương trình cho nhập số điện thoại (S). In ra các số
từ 0 đến 9 không xuất hiện trong số điện thoại vừa nhập.
nhập S=' 0913158020'
Trong số điện thoại 0913158020 không chứa các
ký số: [4, 6, 7]
iv. Cho nhập 1 chuỗi (S). Tìm từ đầu tiên lặp lại trong S.
Ví dụ:

Ví dụ:

S="ab ca bc ab"
S="ab ca bc ca ab bc"
S="ab ca bc"

sẽ in ra ab
sẽ in ra ca
sẽ in ra None
'''
# iii
s = input("Nhập số điện thoại: ")
for i in range(10):
    if str(i) not in s:
        print(i, end=' ')   
print()
# iv
s = input("Nhập chuỗi: ")
for i in range(len(s)):
    if s.count(s[i]) > 1:
        print(s[i])
        break
else:
    print("None")