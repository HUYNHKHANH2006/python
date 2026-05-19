''' 
119/
Số strobogrammatic là số có hình dạng giống nhau khi được xoay 180 độ. Các cặp số strobogrammatic là: (0, 0), (1, 1), (6, 9) và (8, 8).
Ví dụ: 69, 88 và 818 là các số strobogrammatic, nhưng 962 không phải là số strobogrammatic.
Số strobogrammatic mở rộng bao gồm các cặp số strobogrammatic và các cặp số sau: (2, 5) và (5, 2)
. Viết chương trình thực hiện các yêu cầu sau với kiểu dữ liệu cần xử lý là kiểu số nguyên:
a .- In ra các số strobogrammatic nhỏ hơn 1 triệu (1000000).
b .- In ra các số nguyên tố strobogrammatic nhỏ hơn 1 triệu (1000000).
Kết quả sẽ là: 11, 101, 181, 619, 16091, 18181, 19861, 61819, 116911, 119611, 160091,
169691, 191161, 196961, 686989, 688889
c .- In ra các số strobogrammatic mở rộng nhỏ hơn 1 triệu (1000000).
d .- In ra các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu (1000000).
Kết quả sẽ là: 2, 5, 11, 101, 151, 181, 619, 659, 6229, 10501, 12821, 15551, 16091, 18181,
19861, 60209, 60509, 61519, 61819, 62129, 116911, 119611, 160091, 169691,
191161, 196961, 605509, 620029, 625529, 626929, 650059, 655559, 656959,
682289, 686989, 688889, 692269.
e .- In ra các số nhỏ hơn 1 triệu (1000000) không phải là số strobogrammatic và không phải
là số nguyên tố nhưng số strobogrammatic của số này lại là số nguyên tố.
'''

def is_prime(n):
    """Kiểm tra xem n có phải số nguyên tố không"""
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

def get_strobogrammatic_pair(digit, extended=False):
    """Lấy cặp strobogrammatic của một chữ số"""
    pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    if extended:
        pairs['2'] = '5'
        pairs['5'] = '2'
    return pairs.get(digit)

def is_strobogrammatic(num_str, extended=False):
    """Kiểm tra xem số có phải là strobogrammatic không"""
    left, right = 0, len(num_str) - 1
    while left <= right:
        pair = get_strobogrammatic_pair(num_str[left], extended)
        if pair is None or pair != num_str[right]:
            return False
        left += 1
        right -= 1
    return True

def get_strobogrammatic_counterpart(n, extended=False):
    """Lấy số đối xứng strobogrammatic của n"""
    num_str = str(n)
    pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    if extended:
        pairs['2'] = '5'
        pairs['5'] = '2'
    
    result = []
    for digit in num_str:
        if digit not in pairs:
            return None
        result.append(pairs[digit])
    
    result = ''.join(reversed(result))
    return int(result)

def generate_all_strobogrammatic(limit, extended=False):
    """Tạo danh sách tất cả các số strobogrammatic nhỏ hơn limit"""
    result = []
    for n in range(1, limit):
        if is_strobogrammatic(str(n), extended):
            result.append(n)
    return result

# ===== CHƯƠNG TRÌNH CHÍNH =====
limit = 1000000

print("=" * 70)
print("a) Các số strobogrammatic nhỏ hơn 1,000,000:")
print("=" * 70)
strobo_numbers = generate_all_strobogrammatic(limit, extended=False)
print(strobo_numbers)
print(f"Tổng cộng: {len(strobo_numbers)} số\n")

print("=" * 70)
print("b) Các số nguyên tố strobogrammatic nhỏ hơn 1,000,000:")
print("=" * 70)
prime_strobo = [n for n in strobo_numbers if is_prime(n)]
print(prime_strobo)
print(f"Tổng cộng: {len(prime_strobo)} số\n")

print("=" * 70)
print("c) Các số strobogrammatic mở rộng nhỏ hơn 1,000,000:")
print("=" * 70)
strobo_extended = generate_all_strobogrammatic(limit, extended=True)
print(strobo_extended)
print(f"Tổng cộng: {len(strobo_extended)} số\n")

print("=" * 70)
print("d) Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1,000,000:")
print("=" * 70)
prime_strobo_extended = [n for n in strobo_extended if is_prime(n)]
print(prime_strobo_extended)
print(f"Tổng cộng: {len(prime_strobo_extended)} số\n")

print("=" * 70)
print("e) Các số KHÔNG phải strobogrammatic, KHÔNG phải nguyên tố,")
print("   nhưng số strobogrammatic của nó LÀ nguyên tố:")
print("=" * 70)
result_e = []
for n in range(2, limit):
    # Không phải strobogrammatic
    if is_strobogrammatic(str(n), extended=False):
        continue
    # Không phải nguyên tố
    if is_prime(n):
        continue
    # Lấy số đối xứng strobogrammatic
    counterpart = get_strobogrammatic_counterpart(n, extended=False)
    # Số đối xứng phải là nguyên tố
    if counterpart and is_prime(counterpart):
        result_e.append(n)

print(result_e[:100])  # In 100 số đầu tiên
print(f"Tổng cộng: {len(result_e)} số")
