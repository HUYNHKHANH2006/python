"""Viết chương trình cho người dùng nhập 1 chuỗi (S). Tìm xem
nếu từ ‘poor’ đi sau từ ‘not’ thì thay đoạn từ ‘not’ đến ‘poor’
thành duy nhất 1 từ ‘good’. Các trường hợp khác sẽ giữ nguyên
chuỗi (S).
Ví dụ:
S= 'The lyrics is not that poor!'  xuất ra The lyrics is good!
S= 'The lyrics is poor!’  xuất ra The lyrics is poor!
"""
s = input("Nhập chuỗi: ")
not_index = s.find("not") 
poor_index = s.find("poor")
if not_index != -1 and poor_index != -1 and poor_index > not_index:
    s = s[:not_index] + "good" + s[poor_index + len("poor"):]
print(s)