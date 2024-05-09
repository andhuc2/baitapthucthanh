class Polynomial:
    @staticmethod
    def DoiDau(dathuc):
        current = dathuc.head
        while current:
            current.heso *= -1
            current = current.ke_tiep
