'''5.3. Thực hành
Cho nhập chiều dài, chiều rộng và chiều cao của hình khối chữ nhật (theo cm). Tính và xuất kết quả theo ví dụ sau:
	Nhập chiều dài đáy hình chữ nhật (cm):>? 2.134
	Nhập chiều rộng đáy hình chữ nhật (cm):>? 3.4567
	Nhập chiều cao hình khối chữ nhật (cm):>? 4.1
	Số lượng số lẻ cần hiển thị:>? 2
	Diện tích đáy hình chữ nhật = 7.38cm²
	Thể tích hình khối= 30.24cm³
Cho nhập 3 số nguyên a, b, c. In ra 3 số trên theo thứ tự tăng dần
	 Gợi ý: dùng hàm min, max để tìm số nhỏ và lớn nhất và dùng phương thức format của dữ liệu kiểu chuỗi để xuất kết quả.
Cho nhập số nguyên dương a có giá trị từ 1 đến 9. In ra tổng của a + aa + aaa. 
	Ví dụ: a=5  in ra 5 + 55 + 555 = 615

'''
# Nhập chiều dài, chiều rộng và chiều cao của hình khối chữ nhật
length = float(input("nhap chieu dai day hinh chu nhat (cm):>? "))
width = float(input("nhap chieu rong day hinh chu nhat (cm):>? "))
height = float(input("nhap chieu cao hinh khoi chu nhat (cm):>? "))

# Tính và xuất kết quả
area = length * width
volume = area * height
print(f"Diện tích đáy hình chữ nhật = {area:.2f}cm²")
print(f"Thể tích hình khối = {volume:.2f}cm³")
# Nhập 3 số nguyên a, b, c
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
# Sắp xếp và in ra 3 số theo thứ tự tăng dần
sorted_numbers = sorted([a, b, c])
print("3 số theo thứ tự tăng dần:", sorted_numbers)
# Nhập số nguyên dương a
a = int(input("Nhập số nguyên dương a (1-9): "))
# Tính tổng a + aa + aaa  
aa = int(str(a) * 2) 
aaa = int(str(a) * 3)  
total = a + aa + aaa
print(f"{a} + {aa} + {aaa} = {total}")