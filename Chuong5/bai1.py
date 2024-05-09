class BinaryTree:
    class Node:
        def __init__(self, info):
            self.info = info
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Phương thức tính số nút của cây
    def SoNut(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return 1 + self.SoNut(node.left) + self.SoNut(node.right)

# Sử dụng
tree = BinaryTree()
# Thêm các nút vào cây
tree.root = BinaryTree.Node(1)
tree.root.left = BinaryTree.Node(2)
tree.root.right = BinaryTree.Node(3)
tree.root.left.left = BinaryTree.Node(4)
tree.root.left.right = BinaryTree.Node(5)
# Tính số nút của cây
print(tree.SoNut())  # Kết quả: 5
