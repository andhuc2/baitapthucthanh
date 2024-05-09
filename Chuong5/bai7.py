class BinaryTree:
    class Node:
        def __init__(self, info):
            self.info = info
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Phương thức sao chép cây
    def Chep(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return None
        new_node = self.Node(node.info)
        new_node.left = self.Chep(node.left)
        new_node.right = self.Chep(node.right)
        return new_node

# Sử dụng
tree = BinaryTree()
# Thêm các nút vào cây gốc
tree.root = BinaryTree.Node(1)
tree.root.left = BinaryTree.Node(2)
tree.root.right = BinaryTree.Node(3)
# Sao chép cây
new_tree = BinaryTree()
new_tree.root = tree.Chep()
