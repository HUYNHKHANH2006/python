""" 
Tổ chức và xây dựng các hàm cho tất cả các bài thực hành sau:
1) Cho nhập 2 số nguyên a, b trên cùng 1 dòng (cách nhau bởi dấu phẩy - “,'). In ra các
bảng cửu chương từ a đến b (khi a<b) hoặc từ b đến a (khi b<a).
2) Cho nhập số nguyên dương n. Kiểm tra xem n có phải là số nguyên tố hay không?
3) Cho nhập số nguyên dương n. Liệt kê các số nguyên tố < n.
4) Cho nhập số nguyên dương n. Đếm các số nguyên tố <n.
5) Cho nhập số nguyên dương n, liệt kê các ước số của n là số nguyên tố.
Ví dụ: Nhập n=36. Các ước số của 36 gồm 1,2,3,4,6,9,12,18
Nhưng chỉ in ra: Các số vừa là ước số của 36, vừa là số nguyên tố: 2,3
"""
def in_bang_cuu_chuong(a, b):
    # Tìm số nhỏ hơn để bắt đầu, số lớn hơn để kết thúc (xử lý cả 2 trường hợp a<b và b<a)
    start = min(a, b)
    end = max(a, b)
    
    for i in range(start, end + 1):
        print(f"--- Bảng cửu chương {i} ---")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print() 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
    return factors

def main():
    # --- XỬ LÝ BÀI 1 ---
    print("=== BÀI 1 ===")
    chuoi_ab = input("Nhập 2 số nguyên a, b (cách nhau bởi dấu phẩy): ")
    # Tách chuỗi theo dấu phẩy và ép kiểu về số nguyên
    a, b = map(int, chuoi_ab.split(',')) 
    in_bang_cuu_chuong(a, b)

    # --- XỬ LÝ BÀI 2, 3, 4, 5 ---
    print("=== BÀI 2, 3, 4, 5 ===")
    n = int(input("Nhập số nguyên dương n: "))
    
    # Bài 2
    if is_prime(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
    
    # Bài 3
    print(f"Các số nguyên tố < {n}:", end=' ')
    for i in range(2, n):
        if is_prime(i):
            print(i, end=' ')
    print() # Xuống dòng
    
    # Bài 4
    dem = sum(1 for i in range(2, n) if is_prime(i))
    print(f"Số lượng số nguyên tố < {n}: {dem}")
    
    # Bài 5
    factors = prime_factors(n)
    print(f"Các số vừa là ước số của {n}, vừa là số nguyên tố: {', '.join(map(str, factors))}")

if __name__ == "__main__":
    main()