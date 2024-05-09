class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album, bai_hat):
        self.albums[ten_album] = bai_hat

    def XemAlbum(self, ten_album):
        if ten_album in self.albums:
            print("Album:", ten_album)
            for bai_hat, thong_tin in self.albums[ten_album].items():
                print("Bài hát:", bai_hat)
                print("Nhạc sĩ sáng tác:", thong_tin["nhac_si"])
                print("Ca sĩ thể hiện:", thong_tin["ca_si"])
        else:
            print("Không tìm thấy album có tên", ten_album)

# Sử dụng
tu_dien = TuDien()
tu_dien.NhapAlbum("Những bài hát buồn", {
    "Anh sẽ mãi mãi yêu em": {"nhac_si": "Nguyễn Văn A", "ca_si": "Hoàng Thị B"},
    "Lặng yên trong mưa": {"nhac_si": "Trần Văn C", "ca_si": "Phạm Thị D"}
})
tu_dien.XemAlbum("Những bài hát buồn")
