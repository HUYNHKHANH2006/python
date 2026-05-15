'''
110/. Giả sử giữa 2 người A và B có quy ước về việc rút ngắn chuỗi ký tự trong văn bản rõ (plain
text) bằng cách thay thế những ký tự liền kề và giống nhau như sau: ví dụ: plaintext chứa
chuỗi ký tự 'YYYYY' sẽ được thay bằng '#5Y' trong bản mã (cipher text) hay 999.99 sẽ được
thay bằng #39. #29. Giả sử sẽ không có trường hợp có quá 9 ký tự liên tiếp giống nhau.
Viết chương trình Python để khôi phục chuỗi gốc bằng cách nhập chuỗi nén (cipher
text) với quy tắc này. Lưu ý ký tự # không được xuất hiện trong chuỗi ký tự được khôi phục
(plain text).
Ví dụ: cipher text là XY# 6Z1#4023 sẽ xuất ra plain text là XYZZZZZZ1000023
Hay cipher text là #39+1=1#30 sẽ xuất ra plain text là 999+1=1000
'''
def decode_cipher_text(cipher_text):
    plain_text = ""
    i = 0
    while i < len(cipher_text):
        if cipher_text[i] == '#':
            count = int(cipher_text[i + 1])
            char = cipher_text[i + 2]
            plain_text += char * count
            i += 3
        else:
            plain_text += cipher_text[i]
            i += 1
    return plain_text
# Nhập chuỗi nén (cipher text) từ người dùng
cipher_text = input("Nhập chuỗi nén (cipher text): ")
# Khôi phục chuỗi gốc
plain_text = decode_cipher_text(cipher_text)
# In ra chuỗi gốc
print("Chuỗi gốc:", plain_text)