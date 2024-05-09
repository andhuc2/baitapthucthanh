class LinkedList:
    # Định nghĩa cấu trúc Node
    class Node:
        def __init__(self, info):
            self.info = info
            self.next = None

    def __init__(self):
        self.head = None

    # Phương thức đảo ngược danh sách liên kết
    def DaoNguoc(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Sử dụng
dslk = LinkedList()
# Thêm các phần tử vào danh sách liên kết
dslk.head = LinkedList.Node(1)
second = LinkedList.Node(2)
third = LinkedList.Node(3)
dslk.head.next = second
second.next = third
# Đảo ngược danh sách liên kết
dslk.DaoNguoc()
