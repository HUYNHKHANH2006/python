''' 
121/. Viết chương trình cho nhập số nguyên n (2 <= n <= 10), chương trình sẽ phát sinh ra:
a .- Tất cả các số strobogramatic gồm n chữ số.
b .- Tất cả các số strobogramatic mở rộng gồm n chữ số.
'''

def generate_strobogrammatic(n, length, is_extended=False):
    """
    Hàm đệ quy để tạo ra các số strobogrammatic độ dài n.
    length là độ dài gốc để tránh số bắt đầu bằng 0.
    """
    if n == 0:
        return [""]
    if n == 1:
        # Các chữ số tự đối xứng khi xoay 180 độ
        return ["0", "1", "8"]
    
    prev_list = generate_strobogrammatic(n - 2, length, is_extended)
    res = []
    
    # Các cặp strobogrammatic chuẩn
    pairs = [("0", "0"), ("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")]
    
    # Nếu là mở rộng, thêm cặp (2, 5) và (5, 2)
    if is_extended:
        pairs.extend([("2", "5"), ("5", "2")])
    
    for prev in prev_list:
        for p1, p2 in pairs:
            # Không được bắt đầu bằng '0' ở lớp ngoài cùng
            if p1 == "0" and n == length:
                continue
            res.append(p1 + prev + p2)
            
    return res

def main():
    try:
        n = int(input("Nhập số nguyên n (2 <= n <= 10): "))
        if not (2 <= n <= 10):
            print("Vui lòng nhập n trong khoảng từ 2 đến 10.")
            return
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")
        return

    # a) Tất cả các số strobogrammatic gồm n chữ số
    print(f"\na) Các số strobogrammatic gồm {n} chữ số:")
    standard_list = generate_strobogrammatic(n, n, is_extended=False)
    standard_list.sort(key=int)
    print(f"Tìm thấy {len(standard_list)} số:")
    print(standard_list)

    # b) Tất cả các số strobogrammatic mở rộng gồm n chữ số
    print(f"\nb) Các số strobogrammatic mở rộng gồm {n} chữ số:")
    extended_list = generate_strobogrammatic(n, n, is_extended=True)
    extended_list.sort(key=int)
    print(f"Tìm thấy {len(extended_list)} số:")
    print(extended_list)

if __name__ == "__main__":
    main()
