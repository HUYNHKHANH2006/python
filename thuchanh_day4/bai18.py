
# Bài 18: Hàm ẩn danh (lambda) kiểm tra các loại số đặc biệt
import math

# Hàm tính tổng ước số (dùng chung cho d và e) - tối ưu duyệt đến sqrt(n)
def tong_uoc(n):
    total = 1  # 1 luôn là ước
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total if n > 1 else 0


# --- a) Số thân thiện ---
so_than_thien = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

print("=== a) Số thân thiện (1 đến 1,000,000) ===")
ket_qua_a = [n for n in range(1, 1_000_001) if so_than_thien(n)]
print(ket_qua_a[:20], "...")


# --- b) Số chính phương ---
so_chinh_phuong = lambda n: int(math.isqrt(n)) ** 2 == n  # isqrt chính xác hơn sqrt

print("\n=== b) Số chính phương (1 đến 1,000,000) ===")
ket_qua_b = [n for n in range(1, 1_000_001) if so_chinh_phuong(n)]
print(ket_qua_b[:20], "...")


# --- c) Số đồng nhất - Cách 1 dùng all ---
so_dong_nhat = lambda n: all(d == str(n)[0] for d in str(n))

print("\n=== c) Số đồng nhất (1 đến 1,000,000) ===")
ket_qua_c = [n for n in range(1, 1_000_001) if so_dong_nhat(n)]
print(ket_qua_c)


# --- d) Số hoàn thiện - tối ưu dùng tong_uoc ---
so_hoan_thien = lambda n: tong_uoc(n) == n

print("\n=== d) Số hoàn thiện (1 đến 1,000,000) ===")
ket_qua_d = [n for n in range(1, 1_000_001) if so_hoan_thien(n)]
print(ket_qua_d)


# --- e) Số phong phú - tối ưu dùng tong_uoc ---
so_phong_phu = lambda n: tong_uoc(n) > n

print("\n=== e) Số phong phú (1 đến 1,000,000) ===")
ket_qua_e = [n for n in range(1, 1_000_001) if so_phong_phu(n)]
print(ket_qua_e[:20], "...")


# --- f) Số tăng dần ---
so_tang_dan = lambda n: all(str(n)[i] < str(n)[i+1] for i in range(len(str(n))-1))

print("\n=== f) Số tăng dần (1 đến 1,000,000) ===")
ket_qua_f = [n for n in range(1, 1_000_001) if so_tang_dan(n)]
print(ket_qua_f[:20], "...")


# --- g) Số Armstrong ---
so_armstrong = lambda n: sum(int(d) ** len(str(n)) for d in str(n)) == n

print("\n=== g) Số Armstrong (1 đến 1,000,000) ===")
ket_qua_g = [n for n in range(1, 1_000_001) if so_armstrong(n)]
print(ket_qua_g)


# --- h) Số nguyên tố - tối ưu dùng isqrt ---
so_nguyen_to = lambda n: n > 1 and not any(n % i == 0 for i in range(2, math.isqrt(n) + 1))

print("\n=== h) Số nguyên tố (1 đến 1,000,000) ===")
ket_qua_h = [n for n in range(1, 1_000_001) if so_nguyen_to(n)]
print(ket_qua_h[:20], "...")
print(f"Tổng cộng: {len(ket_qua_h)} số nguyên tố")


# --- i) Số Palindrome ---
so_palindrome = lambda n: str(n) == str(n)[::-1]

print("\n=== i) Số Palindrome (1 đến 1,000,000) ===")
ket_qua_i = [n for n in range(1, 1_000_001) if so_palindrome(n)]
print(ket_qua_i[:30], "...")


# --- j) Số nguyên tố Palindrome ---
so_nto_palindrome = lambda n: so_nguyen_to(n) and so_palindrome(n)

print("\n=== j) Số nguyên tố Palindrome (1 đến 1,000,000) ===")
ket_qua_j = [n for n in range(1, 1_000_001) if so_nto_palindrome(n)]
print(ket_qua_j[:30], "...")


# --- k) Số Lộc Phát ---
so_loc_phat = lambda n: all(d in '68' for d in str(n))

print("\n=== k) Số Lộc Phát (1 đến 1,000,000) ===")
ket_qua_k = [n for n in range(1, 1_000_001) if so_loc_phat(n)]
print(ket_qua_k)


# --- l) Số Lộc Phát Palindrome ---
so_lp_palindrome = lambda n: so_loc_phat(n) and so_palindrome(n)

print("\n=== l) Số Lộc Phát Palindrome (1 đến 1,000,000) ===")
ket_qua_l = [n for n in range(1, 1_000_001) if so_lp_palindrome(n)]
print(ket_qua_l)