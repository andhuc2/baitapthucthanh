class Polynomial:
    @staticmethod
    def RutGon(dathuc):
        current = dathuc.head
        while current:
            prev = current
            next_node = current.ke_tiep
            while next_node:
                if next_node.so_mu == current.so_mu:
                    current.heso += next_node.heso
                    prev.ke_tiep = next_node.ke_tiep
                prev = next_node
                next_node = next_node.ke_tiep
            if current.heso == 0:
                dathuc.head = current.ke_tiep
            current = current.ke_tiep
