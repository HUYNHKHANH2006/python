# duyệt từ 2 đến căn bậc 2 của n 
def is_prime(n):
    if n < 2:                               
        return False
    for i in range(2, int(n**0.5) + 1):    
        if n % i == 0:                      
            return False
    return True                            

# 1.n có phải số nguyên tố không
def kiem_tra_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))
    if is_prime(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")


#2.Đếm các số nguyên tố < n
def dem_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))
    dem = sum(1 for i in range(2, n) if is_prime(i))    # Đếm số nguyên tố trong  TỪ 2, n-1
    print(f"Số lượng số nguyên tố < {n}: {dem}")


#  3.Liệt kê các ước số của n  là số nguyên tố
def liet_ke_uoc_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))
    ket_qua = [i for i in range(2, n + 1) if n % i == 0 and is_prime(i)]
    print(f"Các số vừa là ước số {n}, vừa là số nguyên tố: {', '.join(map(str, ket_qua))}")


def main():
    print("Kiểm tra số nguyên tố ")
    kiem_tra_nguyen_to()

    print("\n Đếm số nguyên tố < n ")
    dem_nguyen_to()

    print("\n Ước số nguyên tố của n ")
    liet_ke_uoc_nguyen_to()
main()