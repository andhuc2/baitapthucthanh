class BinaryTree:
    class Node:
        def __init__(self, info):
            self.info = info
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Phương thức tính số nút trung gian của cây
    def SoNutTrungGian(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        if (node.left is None) != (node.right is None):
            return 1 + self.SoNutTrungGian(node.left) + self.SoNutTrungGian(node.right)
        return self.SoNutTrungGian(node.left) + self.SoNutTrungGian(node.right)

# Sử dụng
tree = BinaryTree()
# Thêm các nút vào cây
tree.root = BinaryTree.Node(1)
tree.root.left = BinaryTree.Node(2)
tree.root.right = BinaryTree.Node(3)
tree.root.left.left = BinaryTree.Node(4)
tree.root.left.right = BinaryTree.Node(5)
# Tính số nút trung gian của cây
print(tree.SoNutTrungGian())  # Kết quả: 1
