### em dùng ai ạ 

import datetime
import math
print("=== BÀI i: In thông tin thời gian hiện tại ===")
# Lấy thời gian hiện tại
now = datetime.datetime.now()

# Tính tuần thứ mấy trong tháng: 
# Lấy tuần của năm hiện tại trừ đi tuần của năm tại ngày đầu tiên của tháng + 1
week_of_year_now = int(now.strftime("%W"))
week_of_year_first_day = int(now.replace(day=1).strftime("%W"))
week_of_month = week_of_year_now - week_of_year_first_day + 1

print(f"{'Năm hiện tại':<55} | {now.strftime('%Y')}")
print(f"{'Tháng hiện tại bằng chữ':<55} | {now.strftime('%B')}")
print(f"{'Tuần hiện tại là tuần thứ mấy trong năm':<55} | {now.strftime('%W')}")
print(f"{'Tuần hiện tại là tuần thứ mấy trong tháng':<55} | {week_of_month}")
print(f"{'Ngày hiện tại là ngày thứ mấy trong năm':<55} | {now.strftime('%j')}")
print(f"{'Ngày dương lịch hiện tại là ngày':<55} | {now.strftime('%d')}")
print(f"{'Thứ của ngày hiện tại':<55} | {now.strftime('%A')}")
print(f"{'Giờ phút giây hiện tại':<55} | {now.strftime('%H:%M:%S')}")

print("\n=== BÀI ii: Tính số ngày cách nhau giữa 2 ngày ===")
try:
    d1_str = input("Nhập ngày thứ nhất (dd/mm/yyyy): ")
    d2_str = input("Nhập ngày thứ hai (dd/mm/yyyy): ")
    
    # Chuyển chuỗi sang kiểu datetime
    d1 = datetime.datetime.strptime(d1_str, "%d/%m/%Y")
    d2 = datetime.datetime.strptime(d2_str, "%d/%m/%Y")
    
    # Tính khoảng cách ngày (dùng abs để tránh số âm nếu nhập ngày sau trước)
    delta = abs((d2 - d1).days)
    print(f"-> Số ngày cách nhau giữa 2 ngày là: {delta} ngày")
except ValueError:
    print("-> Vui lòng nhập đúng định dạng dd/mm/yyyy.")


print("\n=== BÀI iii: Chuyển chuỗi sang kiểu ngày ===")
# Chuỗi S theo dạng yêu cầu (VD: 'Sep 18 2019 2:43PM')
S = input("Nhập chuỗi ngày (VD: Sep 18 2019 2:43PM): ")
try:
    # %b: Tháng viết tắt (Sep)
    # %I: Giờ 12h, %p: AM/PM
    date_obj = datetime.datetime.strptime(S, "%b %d %Y %I:%M%p")
    print(f"-> Kiểu ngày sau khi chuyển đổi: {repr(date_obj)}")
except ValueError:
    print("-> Chuỗi nhập vào chưa đúng định dạng yêu cầu.")


print("\n=== BÀI iv: Thêm 5 giây vào thời gian hiện tại ===")
current_time = datetime.datetime.now()
print(f"Thời gian hiện tại: {current_time.strftime('%H:%M:%S')}")

# Sử dụng timedelta để cộng thêm 5 giây
future_time = current_time + datetime.timedelta(seconds=5)
print(f"Thời gian sau khi thêm 5 giây: {future_time.strftime('%H:%M:%S')}")