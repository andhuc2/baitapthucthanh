class Polynomial:
    @staticmethod
    def Them(dathuc, heso, somu):
        new_node = Node(heso, somu)
        if not dathuc:
            dathuc.head = new_node
        else:
            current = dathuc.head
            while current.ke_tiep:
                current = current.ke_tiep
            current.ke_tiep = new_node
