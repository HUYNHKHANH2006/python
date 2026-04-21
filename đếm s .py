#Viết chương trình cho người dùng nhập 1 chuỗi (S) và 1 từ
#(word). Đếm xem trong S có bao nhiêu từ word.
#Ví dụ: kết quả sẽ in: số từ ai là 7 với word=’ai’
#Và s = '''Chiều chiều trước bến Văn Lâu
#Ai ngồi, ai câu, ai sầu, ai thảm
#Ai thương, ai cảm, ai nhớ, ai trông
#Thuyền ai thấp thoáng ven sông
#Đưa câu mái vẩy chạnh lòng nước non '''
s = '''Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm    
Ai thương, ai cảm, ai nhớ, ai trông
Thuyền ai thấp thoáng ven sông
Đưa câu mái vẩy chạnh lòng nước non '''
word = 'ai'
count = 0
words = s.split() # công dụng hàm split để tách chuỗi thành các từ và lưu vào một danh sách
for w in words:
    if w.lower() == word.lower():
        count += 1
print(f'So tu {word} la {count} voi word=\'{word}\'')