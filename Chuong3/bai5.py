class Polynomial:
    @staticmethod
    def Tich(dathuc1, dathuc2):
        result = LinkedList()
        current1 = dathuc1.head
        while current1:
            current2 = dathuc2.head
            while current2:
                heso = current1.heso * current2.heso
                somu = current1.so_mu + current2.so_mu
                Polynomial.Them(result, heso, somu)
                current2 = current2.ke_tiep
            current1 = current1.ke_tiep
        Polynomial.RutGon(result)
        return result
