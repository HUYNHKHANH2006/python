# Nhập chiều dài, chiều rộng và chiều cao của hình khối chữ nhật
length = int(input("Nhập chiều dài đáy hình chữ nhật (cm):>? "))
width = int(input("Nhập chiều rộng đáy hình chữ nhật (cm):>? "))
height = int(input("Nhập chiều cao hình khối chữ nhật (cm):>? "))

# Tính và xuất kết quả
area = length * width
volume = area * height
print(f"Diện tích đáy hình chữ nhật = {area}cm²")
print(f"Thể tích hình khối = {volume}cm³")