class HanoiTower:
    def __init__(self, n):
        self.n = n

    def move(self, source, target, auxiliary, n=None):
        if n is None:
            n = self.n
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
            return
        self.move(source, auxiliary, target, n - 1)
        print(f"Move disk {n} from {source} to {target}")
        self.move(auxiliary, target, source, n - 1)

# Sử dụng
n = 3
tower = HanoiTower(n)
tower.move('A', 'C', 'B')
