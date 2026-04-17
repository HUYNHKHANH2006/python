# Nhập chiều dài, chiều rộng và chiều cao của hình khối chữ nhật
length = int(input("nhap chieu dai day hinh chu nhat (cm):>? "))
width = int(input("nhap chieu rong day hinh chu nhat (cm):>? "))
height = int(input("nhap chieu cao hinh khoi chu nhat (cm):>? "))

# Tính và xuất kết quả
area = length * width
volume = area * height
print(f"Diện tích đáy hình chữ nhật = {area}")
print(f"Thể tích hình khối = {volume}")