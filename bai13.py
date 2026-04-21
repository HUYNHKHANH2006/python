import re

def hoan_chinh(s):
    # Tách chuỗi thành danh sách các dòng để giữ nguyên việc xuống dòng
    lines = s.split('\n')
    
    ket_qua = []
    for line in lines:

        line = line.strip()

        if not line:
            continue

        line = re.sub(r'[ \t]+', ' ', line)
        
        line = re.sub(r' ([.,])', r'\1', line)
        ket_qua.append(line)
        
 
    return '\n'.join(ket_qua)
chuoi_chua_hoan_chinh = """    Quê hương
Quê hương là   chùm khế  ngọt.
  Cho con trèo hái  mỗi ngày .
Quê hương là  đường  đi học .
 Con về rợp bướm vàng bay  .
Đỗ    Trung Quân  """

print(hoan_chinh(chuoi_chua_hoan_chinh))