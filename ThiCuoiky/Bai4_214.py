import math

# Lambda số chính phương
# Số chính phương: căn bậc 2 là số nguyên
so_chinh_phuong = lambda n: n >= 0 and math.isqrt(n) ** 2 == n

# Lambda số hoàn thiện
# Số hoàn thiện: tổng các ước số KHÔNG kể n bằng chính n 
so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

#  các số chính phương từ 1 đến 10000
print("Số chính phương (1 -> 10000): ")
ket_qua_chinh_phuong = [n for n in range(1, 10001) if so_chinh_phuong(n)]
print(ket_qua_chinh_phuong)

# các số hoàn thiện từ 1 đến 10000
print("\n Số hoàn thiện (1 -> 10000): ")
ket_qua_hoan_thien = [n for n in range(1, 10001) if so_hoan_thien(n)]
print(ket_qua_hoan_thien)