from time import sleep
from calculadoraMobileIOS import mobileIosVariables, mobileBasePage
from calculadoraMobileIOS.mobileDriver import mobileDriver

v = mobileIosVariables
p = mobileBasePage.BasePage
d = mobileDriver

dirSoma = '../evidencias/Soma'
dirSubtracao = '../evidencias/Subtracao'
dirMultiplicacao = '../evidencias/Multiplicao'
dirDivisao = '../evidencias/Divisao'

class calculadoraIosPage():
    def soma(self):
        d.criarPastaEvidencia(self,dirSoma)
        p.clicar(self,"id",v.btnUm)
        p.clicar(self, "id", v.btnDois)
        p.clicar(self, "id", v.btnTres)

        p.clicar(self,"id",v.btnSoma)

        p.clicar(self, "id", v.btnQuatro)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSeis)

        d.gerarScreenshot(self, dirSoma, "Ev1")
        p.validarTexto(self, "id", v.txtResultado, "579")
        sleep(1)

        p.clicar(self,"id",v.btnIgual)

        p.clicar(self,"id",v.btnC)

    def subtracao(self):
        d.criarPastaEvidencia(self, dirSubtracao)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSete)
        p.clicar(self, "id", v.btnNove)

        p.clicar(self,"id",v.btnSubtrair)

        p.clicar(self, "id", v.btnQuatro)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSeis)

        d.gerarScreenshot(self, dirSubtracao, "Ev1")
        p.validarTexto(self, "id", v.txtResultado, "123")
        sleep(1)

        p.clicar(self, "id", v.btnIgual)

        p.clicar(self, "id", v.btnC)

    def multiplicao(self):
        d.criarPastaEvidencia(self, dirMultiplicacao)
        p.clicar(self, "id", v.btnTres)
        p.clicar(self, "id", v.btnUm)

        p.clicar(self, "id", v.btnMultiplicar)

        p.clicar(self, "id", v.btnUm)
        p.clicar(self, "id", v.btnZero)

        d.gerarScreenshot(self, dirMultiplicacao, "Ev1")
        p.validarTexto(self, "id", v.txtResultado, "310")
        sleep(1)

        p.clicar(self, "id", v.btnIgual)

        p.clicar(self, "id", v.btnC)

    def divisao(self):
        d.criarPastaEvidencia(self, dirDivisao)
        p.clicar(self, "id", v.btnNove)
        p.clicar(self, "id", v.btnZero)
        p.clicar(self, "id", v.btnZero)

        p.clicar(self, "id", v.btnDivisao)

        p.clicar(self, "id", v.btnZero)

        d.gerarScreenshot(self, dirDivisao, "Ev1")
        p.validarTexto(self,"id",v.txtResultado,"inf")
        sleep(1)
        p.clicar(self, "id", v.btnC)

        p.clicar(self, "id", v.btnNove)
        p.clicar(self, "id", v.btnZero)
        p.clicar(self, "id", v.btnZero)

        p.clicar(self, "id", v.btnDivisao)

        p.clicar(self, "id", v.btnQuatro)

        d.gerarScreenshot(self, dirDivisao, "Ev2")
        p.validarTexto(self, "id", v.txtResultado, "225")

        p.clicar(self, "id", v.btnIgual)

        p.clicar(self, "id", v.btnC)