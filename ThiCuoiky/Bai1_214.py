dai = float(input(" chiều dài đáy hình chữ nhật (cm):"))
rong = float(input(" chiều rộng đáy hình chữ nhật (cm):"))
cao = float(input(" chiều cao hình khối chữ nhật (cm):"))
so_le = int(input("Số lượng số lẻ cần hiển thị:"))

dien_tich = dai * rong
the_tich = dien_tich * cao

print(f"Diện tích đáy hình chữ nhật = {dien_tich:.{so_le}f}cm\u00b2")
print(f"Thể tích hình khối= {the_tich:.{so_le}f}cm\u00b3")