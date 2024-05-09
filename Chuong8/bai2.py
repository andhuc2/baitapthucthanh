class TuDien:
    def __init__(self):
        self.tu_dong_nghia = {}
        self.tu_trai_nghia = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        hash_key = tu[0].lower()
        if dong_nghia:
            self.tu_dong_nghia[tu] = dong_nghia
        if trai_nghia:
            self.tu_trai_nghia[tu] = trai_nghia

    def DongNghia(self, tu):
        return self.tu_dong_nghia.get(tu, [])

    def TraiNghia(self, tu):
        return self.tu_trai_nghia.get(tu, [])

# Sử dụng
tu_dien = TuDien()
tu_dien.NhapTu("tốt", ["tuyệt vời", "tốt lắm", "xuất sắc"], ["xấu", "tệ"])
dong_nghia = tu_dien.DongNghia("tốt")
trai_nghia = tu_dien.TraiNghia("tốt")
print("Các từ đồng nghĩa của 'tốt':", dong_nghia)
print("Các từ trái nghĩa của 'tốt':", trai_nghia)
