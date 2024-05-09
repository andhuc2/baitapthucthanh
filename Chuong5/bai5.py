class BinaryTree:
    class Node:
        def __init__(self, info):
            self.info = info
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Phương thức kiểm tra cây có phải là cây BST hay không
    def KiemTraBST(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True
        if not (min_val <= node.info <= max_val):
            return False
        return (self.KiemTraBST(node.left, min_val, node.info - 1) and
                self.KiemTraBST(node.right, node.info + 1, max_val))

# Sử dụng
tree = BinaryTree()
# Thêm các nút vào cây
tree.root = BinaryTree.Node(2)
tree.root.left = BinaryTree.Node(1)
tree.root.right = BinaryTree.Node(3)
# Kiểm tra cây có phải là BST hay không
print(tree.KiemTraBST())  # Kết quả: True
