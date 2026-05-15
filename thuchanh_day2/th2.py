def is_prime(n):
    """Kiểm tra xem n có phải số nguyên tố hay không"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    """Kiểm tra xem n có phải số đối xứng hay không"""
    s = str(n)
    return s == s[::-1]

def find_sacred_numbers(a, b):
    """Tìm tất cả số thần thiêng trong khoảng [a, b]"""
    sacred_numbers = []
    for num in range(a, b + 1):
        if is_prime(num) and is_palindrome(num):
            sacred_numbers.append(num)
    return sacred_numbers

# Nhập dữ liệu
a, b = map(int, input("Nhập hai số nguyên a, b (10 ≤ a ≤ b ≤ 30000): ").split())

# Tìm các số thần thiêng
result = find_sacred_numbers(a, b)

# In kết quả
if result:
    print(f"\nCác số thần thiêng trong khoảng [{a}, {b}]:")
    print(result)
    print(f"\nSố lượng: {len(result)}")
else:
    print(f"\nKhông có số thần thiêng trong khoảng [{a}, {b}]")