class Polynomial:
    @staticmethod
    def Cong(dathuc1, dathuc2):
        result = LinkedList()
        current1 = dathuc1.head
        current2 = dathuc2.head
        while current1 and current2:
            if current1.so_mu == current2.so_mu:
                heso_sum = current1.heso + current2.heso
                if heso_sum != 0:
                    Polynomial.Them(result, heso_sum, current1.so_mu)
                current1 = current1.ke_tiep
                current2 = current2.ke_tiep
            elif current1.so_mu < current2.so_mu:
                Polynomial.Them(result, current1.heso, current1.so_mu)
                current1 = current1.ke_tiep
            else:
                Polynomial.Them(result, current2.heso, current2.so_mu)
                current2 = current2.ke_tiep
        while current1:
            Polynomial.Them(result, current1.heso, current1.so_mu)
            current1 = current1.ke_tiep
        while current2:
            Polynomial.Them(result, current2.heso, current2.so_mu)
            current2 = current2.ke_tiep
        Polynomial.RutGon(result)
        return result
