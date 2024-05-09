class Polynomial:
    @staticmethod
    def Chep(dathuc):
        result = LinkedList()
        current = dathuc.head
        while current:
            Polynomial.Them(result, current.heso, current.so_mu)
            current = current.ke_tiep
        return result
