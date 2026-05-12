'''
có 9 loại tiền đồng: 1, 2, 5, 10, 20, 50, 100, 200, 500 đồng.cho 
nhập số tiền x,  chuyển số tiền x ra các loại tiền sao cho số lượng là ít nhất. in ra số tờ tiền của mỗi loại, tổng số tờ tiền của
tất cả các loại 
ví dụ
nhập x: 1234 sẻ in ra 
so tien 1234 duoc chuyen doi thanh:
loai tien 500: 2 to
loai tien 200: 1 to
loai tien 100: 0 to
loai tien 50: 0 to
loai tien 20: 1 to
loai tien 10: 1 to
loai tien 5: 0 to
loai tien 2: 2 to
loai tien 1: 0 to
tong so to tien: 7 to
'''''
def chuyen_doi_tien(x, loai_tien):
    so_to_tien = []
    tong_so_to = 0

    for tien in loai_tien:
        so_to = x // tien 
        so_to_tien.append(so_to) 
        tong_so_to += so_to
        x -= so_to * tien

    return so_to_tien, tong_so_to

# Định nghĩa loai_tien
loai_tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

x = int(input("Nhap so tien: "))
so_to_tien, tong_so_to = chuyen_doi_tien(x, loai_tien)

print(f"So tien {x} duoc chuyen doi thanh:")
for i in range(len(loai_tien)):
    print(f"Loai tien {loai_tien[i]}: {so_to_tien[i]} to")

print(f"Tong so to tien: {tong_so_to} to")
