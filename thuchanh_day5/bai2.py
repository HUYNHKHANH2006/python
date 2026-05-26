"""
Viết chương trình Python sử dụng lambda để tính cho các trường hợp sau:
1) Hàm nhận 1 đối số là số nguyên n và trả về trị tuyệt đối của n.
2) Hàm nhận 1 đối số là số nguyên n và trả về giá trị của n+15.
3) Hàm nhận 2 đối số là số nguyên (x, y), trả về tích của x và y.
4) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là bội số của 13 hoặc 19 hay không?
5) Hàm nhận 1 đối số là số thực r là bán kính của hình tròn. Cho biết diện tích hình tròn.
6) Hàm nhận 2 đối số là số thực d, r là chiều dài và chiều rộng của hình chữ nhật. Cho biết chu vi hình
chữ nhật.
7) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số chính phương hay không? (số chính phương
là số có căn bậc hai là 1 số nguyên như: 4, 9, 16, ... ).
8) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số nguyên tố hay không?
9) Hàm nhận 3 tham số là số nguyên (a, b, c). Cho biết a, b, c có là 3 cạnh hợp lệ của 1 tam giác hay
không? Nếu là 3 cạnh hợp lệ của tam giác, cho biết đó là tam giác gì? (thường, cân, đều, vuông, ... ).
"""
import math

# --- KHAI BÁO CÁC HÀM LAMBDA ---

bai_1 = lambda n: abs(n)
bai_2 = lambda n: n + 15
bai_3 = lambda x, y: x * y
bai_4 = lambda n: n % 13 == 0 or n % 19 == 0
bai_5 = lambda r: math.pi * (r ** 2)
bai_6 = lambda d, r: 2 * (d + r)
bai_7 = lambda n: n >= 0 and int(n**0.5)**2 == n
bai_8 = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

bai_9 = lambda a, b, c: (
    "Không hợp lệ" if not (a + b > c and a + c > b and b + c > a) 
    else ("Tam giác Đều" if a == b == c 
    else ("Tam giác Vuông Cân" if (a == b or b == c or a == c) and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) 
    else ("Tam giác Vuông" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 
    else ("Tam giác Cân" if a == b or b == c or a == c 
    else "Tam giác Thường"))))
)


print("Bài 1:", bai_1(-10))                  
print("Bài 2:", bai_2(5))                    
print("Bài 3:", bai_3(4, 5))                 
print("Bài 4:", bai_4(38))                  
print("Bài 5:", bai_5(3))                    
print("Bài 6:", bai_6(4, 6))                
print("Bài 7:", bai_7(16))                  
print("Bài 8:", bai_8(17))                  
print("Bài 9:", bai_9(3, 4, 5))              
print("Bài 9:", bai_9(5, 5, 5))             