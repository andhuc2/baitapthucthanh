class BinaryTree:
    class Node:
        def __init__(self, info):
            self.info = info
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Phương thức tính số nút lá của cây
    def SoNutLa(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.SoNutLa(node.left) + self.SoNutLa(node.right)

# Sử dụng
tree = BinaryTree()
# Thêm các nút vào cây
tree.root = BinaryTree.Node(1)
tree.root.left = BinaryTree.Node(2)
tree.root.right = BinaryTree.Node(3)
tree.root.left.left = BinaryTree.Node(4)
tree.root.left.right = BinaryTree.Node(5)
# Tính số nút lá của cây
print(tree.SoNutLa())  # Kết quả: 3
