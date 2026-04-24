'''Viết hàm nhận tham số là 1 số nguyên dương (n). Tính
số hạng thứ n của chuỗi Fibonaci.
Ví dụ với n=7 sẽ in ra số 13, n=8 sẽ in ra 21, ...
– Nhắc lại chuỗi số Fibonacci: 1 1 2 3 5 8 13 ...
Dãy Fibonaci được định nghĩa truy hồi như sau:
F0 = F1 = 1
Fn = Fn-1 + Fn-2 nếu n>=2
'''
def fibonacci(n):
    if n <= 0:
        return "nhập vào số dương."
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("nhập vào số nguyên dương: "))
print(fibonacci(n))