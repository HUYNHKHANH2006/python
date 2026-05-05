'''
3.12. Thực hành
ii. Cho nhập 2 chuỗi (S1 và S2).
a) In ra những ký tự xuấtt hiện trong cả 2 chuỗi.
Gợi ý: sử dụng class Counter trong module collections
để chuyển mỗi chuỗi vào 1 dict thuộc class Counter.
Thực hiện phép và (&) trên 2 dict này để có kết quả.
b) Đếm xem có bao nhiêu ký tự có trong S1 nhưng không
có trong S2 và có trong S2 nhưng không có trong S1.
c) In ra những ký tự có trong S1 nhưng không có trong S2
và những ký tự có trong S2 nhưng không có trong S1.
Gơi ý: đưa mỗi chuỗi vào 1 dict (dictl và dict2). Thực
hiện dò tìm S1 trên dict2 và tìm S2 trên dict1.

文A    
'''
from collections import Counter
s1 = input("Nhap chuoi s1: ")
s2 = input("Nhap chuoi s2: ")
dict1 = Counter(s1)
dict2 = Counter(s2)
print("a)", dict1 & dict2)
print("b)", dict1 - dict2)
print("c)", set(s1) ^ set(s2))