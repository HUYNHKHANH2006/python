'''
7.5. Thực hành hàm đệ quy
1) Cho nhập số nguyên n. Tính tổng các chữ số có trong n.
Ví dụ: n=345  tổng = 12.
2) Viết hàm tính giai thừa (factorial number) của một số
nguyên dương (n).
Với 1! = 1; 2! = 1 x 2; 3! = 1 x 2 x 3; ... n! = 1 x 2 x 3 x ... x n
3) Viết hàm nhận 2 tham số là 2 số nguyên dương a, b.
Tính a^b. Ví dụ: a=2, b=3  2^3=8
4) Viết hàm nhận 2 tham số là 2 số nguyên dương a, b. Tìm
ước số chung lớn nhất (greatest common divisor -gcd)
của a và b.
'''
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))
# Tính tổng các chữ số có trong n
total = sum_of_digits(n)
print(f"Tóng các chữ số có trong {n} = {total}")
# Tính giai thừa của một số nguyên dương n
if n > 0:
    fact = factorial(n)
    print(f"Giai thừa của {n} = {fact}")
else:
    print("Vui lòng nhập số nguyên dương cho giai thừa.")
# Tính a^b
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
result = power(a, b)
print(f"{a}^{b} = {result}")
# Tìm số chung lớn nhất
c = int(input("Nhập số nguyên dương c: "))
d = int(input("Nhập số nguyên dương d: "))
gcd_result = gcd(c, d)
print(f"So chung lon nhat cua {c} va {d} la: {gcd_result}")