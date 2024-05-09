class BinaryTree:
    class Node:
        def __init__(self, info):
            self.info = info
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Phương thức tính chiều cao của một nút
    def ChieuCao(self, node=None):
        if node is None:
            return 0
        return 1 + max(self.ChieuCao(node.left), self.ChieuCao(node.right))

    # Phương thức kiểm tra cây có phải là cây AVL hay không
    def KiemTraAVL(self):
        def is_AVL(node):
            if node is None:
                return True
            return (abs(self.ChieuCao(node.left) - self.ChieuCao(node.right)) <= 1 and
                    is_AVL(node.left) and is_AVL(node.right))
        return is_AVL(self.root)

# Sử dụng
tree = BinaryTree()
# Thêm các nút vào cây
tree.root = BinaryTree.Node(1)
tree.root.left = BinaryTree.Node(2)
tree.root.right = BinaryTree.Node(3)
# Kiểm tra cây có phải là cây AVL hay không
print(tree.KiemTraAVL())  # Kết quả: True
