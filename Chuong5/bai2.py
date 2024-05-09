class BinaryTree:
    class Node:
        def __init__(self, info):
            self.info = info
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Phương thức tính chiều cao của cây
    def ChieuCao(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return 1 + max(self.ChieuCao(node.left), self.ChieuCao(node.right))

# Sử dụng
tree = BinaryTree()
# Thêm các nút vào cây
tree.root = BinaryTree.Node(1)
tree.root.left = BinaryTree.Node(2)
tree.root.right = BinaryTree.Node(3)
tree.root.left.left = BinaryTree.Node(4)
tree.root.left.right = BinaryTree.Node(5)
# Tính chiều cao của cây
print(tree.ChieuCao())  # Kết quả: 3
