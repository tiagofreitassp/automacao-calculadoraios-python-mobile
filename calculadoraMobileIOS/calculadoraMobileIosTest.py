import unittest
from calculadoraMobileIOS import calculadoraMobileIosPage, mobileDriver

d = mobileDriver.mobileDriver
p = calculadoraMobileIosPage.calculadoraIosPage

class calculadoraMobileTest(unittest.TestCase):
    def setUp(self):
        d.criarDriver(self)

    def tearDown(self):
        d.fecharDriver(self)

    def test1_Soma(self):
        p.soma(self)

    def test2_Subtracao(self):
        p.subtracao(self)

    def test3_Multiplicacao(self):
        p.multiplicao(self)

    def test4_Divisao(self):
        p.divisao(self)

if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(calculadoraMobileTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
