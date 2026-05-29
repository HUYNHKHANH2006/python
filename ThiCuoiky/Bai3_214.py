import math
# Lambda
# Số chính phương: căn bậc 2 là số nguyên
so_chinh_phuong = lambda n: n >= 0 and int(math.isqrt(n)) ** 2 == n

# xác định loại tam giác từ 3 cạnh a, b, c
tam_giac = lambda a, b, c: (
    "Không hợp lệ"          if not (a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a)
    else "Tam giác đều"     if a == b == c
    else "Tam giác vuông cân" if (a == b or b == c or a == c) and sorted([a,b,c])[0]**2 + sorted([a,b,c])[1]**2 == sorted([a,b,c])[2]**2
    else "Tam giác vuông"   if sorted([a,b,c])[0]**2 + sorted([a,b,c])[1]**2 == sorted([a,b,c])[2]**2
    else "Tam giác cân"     if a == b or b == c or a == c
    else "Tam giác thường"
)

# Kiểm tra số chính phương
n = int(input("Nhập số nguyên n: "))
if so_chinh_phuong(n):
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")

# Kiểm tra tam giác
a, b, c = map(int, input("Nhập 3 cạnh a b c (cách nhau bởi dấu cách): ").split())
print(tam_giac(a, b, c))