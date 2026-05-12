def chuyen_doi_tien(x, loai_tien):
    so_to_tien = []
    tong_so_to = 0
    tong_so_loai = 0 # Biến mới để đếm xem dùng bao nhiêu loại tiền khác nhau

    for tien in loai_tien:
        so_to = x // tien
        so_to_tien.append(so_to) 
        
        if so_to > 0:
            tong_so_to += so_to
            tong_so_loai += 1
            
        x -= so_to * tien

    return so_to_tien, tong_so_to, tong_so_loai

loai_tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

a = int(input("Nhập số tiền hàng cần thanh toán (a): "))
b = int(input("Nhập số tiền khách thực tế trả (b): "))

if a > b:
    tien_thieu = a - b
    print(f"Số tiền khách hàng còn thiếu là {tien_thieu}")
elif a == b:
    print("Cám ơn khách hàng. Hẹn gặp lại")
else:
    tien_thoi = b - a
    print(f"Số tiền {tien_thoi} được thối lại thành:")
    
    so_to_tien, tong_so_to, tong_so_loai = chuyen_doi_tien(tien_thoi, loai_tien)
    
    for i in range(len(loai_tien)):
        if so_to_tien[i] > 0:
            print(f"Loại {loai_tien[i]} gồm {so_to_tien[i]} tờ")
            
    print(f"Tổng cộng có {tong_so_to} tờ")
    print(f"Tổng số loại = {tong_so_loai}")
    
    input("Nhấn phím Enter để tiếp tục...")
    print("Cám ơn khách hàng. Hẹn gặp lại")