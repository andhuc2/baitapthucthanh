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

    def TraTu(self, tu):
        dong_nghia = self.tu_dong_nghia.get(tu)
        trai_nghia = self.tu_trai_nghia.get(tu)
        return dong_nghia, trai_nghia

# Sử dụng
tu_dien = TuDien()
tu_dien.NhapTu("học", ["nghiên cứu", "thu thập"], ["ngừng", "bỏ"])
dong_nghia, trai_nghia = tu_dien.TraTu("học")
print("Đồng nghĩa của từ 'học':", dong_nghia)
print("Trái nghĩa của từ 'học':", trai_nghia)
