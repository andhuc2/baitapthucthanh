class Nghia:
    def __init__(self, loai_tu, nghia, vi_du):
        self.loai_tu = loai_tu
        self.nghia = nghia
        self.vi_du = vi_du
        self.tiep_theo = None

class Tu:
    def __init__(self, tu):
        self.tu = tu
        self.nghia_dau = None
    
    def them_nghia(self, loai_tu, nghia, vi_du):
        if not self.nghia_dau:
            self.nghia_dau = Nghia(loai_tu, nghia, vi_du)
        else:
            current = self.nghia_dau
            while current.tiep_theo:
                current = current.tiep_theo
            current.tiep_theo = Nghia(loai_tu, nghia, vi_du)

class TuDien:
    def __init__(self):
        self.root = None

    def them_tu(self, tu, loai_tu, nghia, vi_du):
        if not self.root:
            self.root = Tu(tu)
        else:
            self._them_tu(self.root, tu, loai_tu, nghia, vi_du)

    def _them_tu(self, current, tu, loai_tu, nghia, vi_du):
        if tu < current.tu:
            if not current.left:
                current.left = Tu(tu)
            else:
                self._them_tu(current.left, tu, loai_tu, nghia, vi_du)
        elif tu > current.tu:
            if not current.right:
                current.right = Tu(tu)
            else:
                self._them_tu(current.right, tu, loai_tu, nghia, vi_du)
        else:
            current.them_nghia(loai_tu, nghia, vi_du)

    def tim_tu(self, tu):
        return self._tim_tu(self.root, tu)

    def _tim_tu(self, current, tu):
        if not current:
            return None
        if tu == current.tu:
            return current
        elif tu < current.tu:
            return self._tim_tu(current.left, tu)
        else:
            return self._tim_tu(current.right, tu)

    def loai_bo_tu(self, tu):
        self.root = self._loai_bo_tu(self.root, tu)

    def _loai_bo_tu(self, current, tu):
        if not current:
            return None
        if tu == current.tu:
            if not current.left and not current.right:
                return None
            if not current.left:
                return current.right
            if not current.right:
                return current.left
            min_node = self._tim_node_nho_nhat(current.right)
            current.tu = min_node.tu
            current.right = self._loai_bo_tu(current.right, min_node.tu)
        elif tu < current.tu:
            current.left = self._loai_bo_tu(current.left, tu)
        else:
            current.right = self._loai_bo_tu(current.right, tu)
        return current

    def _tim_node_nho_nhat(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def luu_vao_tap_tin(self, ten_tap_tin):
        with open(ten_tap_tin, 'w') as file:
            self._luu_node_vao_tap_tin(self.root, file)

    def _luu_node_vao_tap_tin(self, node, file):
        if node:
            file.write(node.tu + '\n')
            self._luu_nghia_vao_tap_tin(node.nghia_dau, file)
            self._luu_node_vao_tap_tin(node.left, file)
            self._luu_node_vao_tap_tin(node.right, file)

    def _luu_nghia_vao_tap_tin(self, nghia, file):
        while nghia:
            file.write(f"{nghia.loai_tu}: {nghia.nghia}\n")
            file.write(f"Ví dụ: {nghia.vi_du}\n")
            nghia = nghia.tiep_theo

    def nap_tu_tap_tin(self, ten_tap_tin):
        with open(ten_tap_tin, 'r') as file:
            lines = file.readlines()
            tu = None
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if not tu:
                    tu = line
                else:
                    if line.startswith(':'):
                        loai_tu = line.split(':')[1].strip()
                    elif line.startswith('Ví dụ:'):
                        vi_du = line.split(':')[1].strip()
                        self.them_tu(tu, loai_tu, nghia, vi_du)
                        tu = None
                    else:
                        nghia = line.split(':')[1].strip()

# Hàm main để kiểm tra các chức năng
def main():
    tu_dien = TuDien()
    tu_dien.them_tu("hello", "danh từ", "lời chào", "Hello, how are you?")
    tu_dien.them_tu("run", "động từ", "chạy", "He runs very fast.")
    tu_dien.them_tu("big", "tính từ", "lớn", "That's a big house.")
    
    while True:
        print("\nMenu:")
        print("1. Thêm một mục từ mới vào từ điển")
        print("2. Loại bỏ một mục từ của từ điển")
        print("3. Tra cứu các nghĩa của một mục từ trong từ điển")
        print("4. Lưu từ điển vào tập tin")
        print("5. Nạp từ điển từ tập tin")
        print("6. Kết thúc chương trình")

        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            tu = input("Nhập từ: ")
            loai_tu = input("Nhập loại từ: ")
            nghia = input("Nhập nghĩa: ")
            vi_du = input("Nhập ví dụ: ")
            tu_dien.them_tu(tu, loai_tu, nghia, vi_du)
            print("Đã thêm từ vào từ điển!")

        elif choice == '2':
            tu = input("Nhập từ cần loại bỏ: ")
            tu_dien.loai_bo_tu(tu)
            print("Đã loại bỏ từ khỏi từ điển!")

        elif choice == '3':
            tu = input("Nhập từ cần tra cứu: ")
            node = tu_dien.tim_tu(tu)
            if node:
                print("Từ:", node.tu)
                current = node.nghia_dau
                while current:
                    print(f"Loại từ: {current.loai_tu}")
                    print(f"Nghĩa: {current.nghia}")
                    print(f"Ví dụ: {current.vi_du}")
                    current = current.tiep_theo
            else:
                print("Từ không tồn tại trong từ điển!")

        elif choice == '4':
            ten_tap_tin = input("Nhập tên tập tin để lưu từ điển: ")
            tu_dien.luu_vao_tap_tin(ten_tap_tin)
            print("Đã lưu từ điển vào tập tin!")

        elif choice == '5':
            ten_tap_tin = input("Nhập tên tập tin để nạp từ điển: ")
            tu_dien.nap_tu_tap_tin(ten_tap_tin)
            print("Đã nạp từ điển từ tập tin!")

        elif choice == '6':
            print("Kết thúc chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
