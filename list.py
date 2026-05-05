'''
1. LIST

1.16. Thực hành
vii. Viết chương trình cho người dùng nhập nhiều lần các số nguyên
dương. Sau mỗi lần nhập, chương trình sẽ hỏi người dùng có
muốn nhập nữa hay không (Yes/No). Nếu chọn Yes (Y) thì cho
người dùng nhập tiếp. Ngược lại nếu chọn No (N), chương trình
sẽ thực hiện:
a) In ra các số nguyên tố có trong list.
b) Tính trung bình cộng các số âm, trung bình các số dương
c) Số lớn nhất, số nhỏ nhất
d) Cho biết các số trong list có được sắp xếp tăng dần hay chưa?
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhap so luong so nguyen: "))
numbers = []
while n > 0:
    number = int(input("Nhap so nguyen: "))
    if is_prime(number):
        numbers.append(number)
    n -= 1

print("cac so nguyen to la:", numbers)  
print("trung binh cong cac so am la:", sum([x for x in numbers if x < 0]) / len([x for x in numbers if x < 0]))
print("trung binh cong cac so duong la:", sum([x for x in numbers if x > 0]) / len([x for x in numbers if x > 0]))
print("so lon nhat la:", max(numbers))
print("so nho nhat la:", min(numbers))
if numbers == sorted(numbers):
    print("cac so da duoc sap xep tang dan")
else:    print("cac so chua duoc sap xep tang dan")
