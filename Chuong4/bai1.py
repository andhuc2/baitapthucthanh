class LinkedList:
    # Định nghĩa cấu trúc Node
    class Node:
        def __init__(self, info):
            self.info = info
            self.next = None

    def __init__(self):
        self.head = None

    # Phương thức in ngược danh sách liên kết đệ qui
    def InNguocRecursive(self, node):
        if node is None:
            return
        self.InNguocRecursive(node.next)
        print(node.info)

    # Phương thức in ngược danh sách liên kết không đệ qui
    def InNguoc(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.info)
            current = current.next
        while stack:
            print(stack.pop())

# Sử dụng
dslk = LinkedList()
# Thêm các phần tử vào danh sách liên kết
dslk.head = LinkedList.Node(1)
second = LinkedList.Node(2)
third = LinkedList.Node(3)
dslk.head.next = second
second.next = third
# In ngược danh sách liên kết
dslk.InNguoc()
