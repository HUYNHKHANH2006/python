''''Thực hành
4) Cho nhập số nguyên dương n. Đếm số lượng chữ số chẵn, số chữ
số lẻ có trong n.
• Ví dụ: n=5084  số lượng số lẻ:1, số lượng số chẵn:3
5) Tính tổng và tích các chữ số của số nguyên dương n.
• Ví dụ: n=5084  in ra tổng=17, tích=0
6) Tìm chữ số lớn nhất có trong số nguyên dương n.
• Ví dụ: n=5084  in ra số lớn nhất=8
7) Số may mắn: giả sử người ta cho rằng 1 số gọi là số may mắn
nếu chỉ chứa toàn các số 6 hoặc số 8. Viết chương trình cho nhập
số nguyên n, xét xem n có là số may mắn hay không?
• Ví dụ: n=686  686 là số may mắn.
n=68626  68626 KHÔNG phải số may mắn.
'''
n = int(input("Nhập số nguyên dương n: "))
even_count = 0
odd_count = 0
digit_sum = 0
max_digit = 0
# Đếm số lượng chữ số chẵn, số chữ số lẻ, tính tổng và tích các chữ số, tìm chữ số lớn nhất
for digit in str(n):
    digit = int(digit)
    digit_sum += digit
    if digit > max_digit:
        max_digit = digit
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
# In ra số lượng số lẻ, số lượng số chẵn, tổng và tích các chữ số, chữ số lớn nhất
print(f"So luong so le: {odd_count}")
print(f"So luong so chan: {even_count}")
print(f"Tong cac chu so: {digit_sum}")
print(f"Tich cac chu so: {digit_sum}")
print(f"Chu so lon nhat: {max_digit}")
# Kiểm tra xem n có phải là số may mắn hay không
is_lucky = all(digit in '68' for digit in str(n))
print(f"{n} {'la so may man' if is_lucky else 'khong phai so may man'}")