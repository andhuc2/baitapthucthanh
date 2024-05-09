class BinaryTree:
    class Node:
        def __init__(self, info):
            self.info = info
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Phương thức so sánh hai cây
    def SoSanh(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None:
            return (node1.info == node2.info and
                    self.SoSanh(node1.left, node2.left) and
                    self.SoSanh(node1.right, node2.right))
        return False

# Sử dụng
tree1 = BinaryTree()
# Thêm các nút vào cây 1
tree1.root = BinaryTree.Node(1)
tree1.root.left = BinaryTree.Node(2)
tree1.root.right = BinaryTree.Node(3)

tree2 = BinaryTree()
# Thêm các nút vào cây 2
tree2.root = BinaryTree.Node(1)
tree2.root.left = BinaryTree.Node(2)
tree2.root.right = BinaryTree.Node(3)

# So sánh hai cây
print(tree1.SoSanh(tree1.root, tree2.root))  # Kết quả: True
