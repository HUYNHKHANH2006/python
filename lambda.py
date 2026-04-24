'''
6. Anonymous Function (lambda)
THỰC HÀNH
1. Viết chương trình Python sử dụng lambda để tính cho các trường hợp sau:
a) Hàm nhận 1 đối số là số nguyên n và trả về trị tuyệt đối của n.
b) Hàm nhận 1 đối số là số nguyên n và trả về giá trị của n+15.
c) Hàm nhận 2 đối số là số nguyên (x, y), trả về tích của x và y.
d) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là bội số của 13 hoặc 19 hay
không?
e) Hàm nhận 1 đối số là số thực r là bán kính của hình tròn. Cho biết diện tích hình
tròn.
1) Hàm nhận 2 đối số là số thực d, r là chiều dài và chiều rộng của hình chữ nhật.
Cho biết chu vi hình chữ nhật.
g Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số chính phương hay không?
(số chính phương là số có căn bậc hai là 1 số nguyên như: 4, 9, 16, ... ).
h) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số nguyên tố hay không?
i) Hàm nhận 3 tham số là số nguyên (a, b, c). Cho biết a, b, c có là 3 cạnh hợp lệ
của 1 tam giác hay không? Nếu là 3 cạnh hợp lệ của tam giác, cho biết đó là tam
giác gì? (thường, cân, đều, vuông, ... ).
'''
import math

# a) Hàm nhận 1 đối số là số nguyên n và trả về trị tuyệt đối của n.
abs_value = lambda n: abs(n)
print("a)", abs_value(-20))

# b) Hàm nhận 1 đối số là số nguyên n và trả về giá trị của n+15.
add_15 = lambda n: n + 15
print("b)", add_15(5))

# c) Hàm nhận 2 đối số là số nguyên (x, y), trả về tích của x và y.
multiply = lambda x, y: x * y
print("c)", multiply(2, 3))

# d) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là bội số của 13 hoặc 19 hay không?
is_multiple_of_13_or_19 = lambda n: n % 13 == 0 or n % 19 == 0
print("d)", is_multiple_of_13_or_19(26))

# e) Hàm nhận 1 đối số là số thực r là bán kính của hình tròn. Cho biết diện tích hình tròn.
area_of_circle = lambda r: math.pi * r ** 2
print("e)", area_of_circle(5))

# f) Hàm nhận 2 đối số là số thực d, r là chiều dài và chiều rộng của hình chữ nhật. Cho biết chu vi.
perimeter_of_rectangle = lambda d, r: 2 * (d + r)
print("f)", perimeter_of_rectangle(2, 3))

# g) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số chính phương hay không?
# Sửa: Thêm n >= 0 để tránh lỗi toán học khi tính căn bậc 2 của số âm
is_perfect_square = lambda n: n >= 0 and int(math.sqrt(n)) ** 2 == n
print("g)", is_perfect_square(4))

# h) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số nguyên tố hay không?
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
print("h)", is_prime(7))

# i) Hàm nhận 3 tham số là số nguyên (a, b, c). Cho biết loại tam giác.
# Sửa: Dùng if-else lồng nhau (Ternary operator) để gom vào 1 dòng lambda
triangle_type = lambda a, b, c: (
    (
        "Tam giác đều" if a == b == c else
        "Tam giác vuông" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else
        "Tam giác cân" if a == b or b == c or a == c else
        "Tam giác thường"
    ) if (a + b > c and a + c > b and b + c > a) else "Không phải tam giác"
)

print("i)", triangle_type(3, 4, 5))  #  Tam giác vuông
print("i)", triangle_type(5, 5, 5))  #  Tam giác đều
print("i)", triangle_type(1, 2, 3))  #  Không phải tam giác