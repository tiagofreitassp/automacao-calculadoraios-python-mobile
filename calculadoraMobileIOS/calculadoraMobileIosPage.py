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
        p.clicar(self, "id", v.btnC)

        p.clicar(self,"id",v.btnUm)
        p.clicar(self, "id", v.btnDois)
        p.clicar(self, "id", v.btnTres)

        sleep(1)
        d.gerarScreenshot(self, dirSoma, "Ev1")
        p.clicar(self,"id",v.btnSoma)

        p.clicar(self, "id", v.btnQuatro)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSeis)

        d.gerarScreenshot(self, dirSoma, "Ev2")

        p.clicar(self,"id",v.btnIgual)
        sleep(1)
        d.gerarScreenshot(self, dirSoma, "Ev3")
        p.validarTexto(self, "id", v.txtResultado, "579")
        sleep(1)

        p.clicar(self,"id",v.btnC)
        d.criarDocumentoDeEvidencia(self, dirSoma, "CT01", "Cálculo Soma Android")

    def subtracao(self):
        d.criarPastaEvidencia(self, dirSubtracao)
        p.clicar(self, "id", v.btnC)

        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSete)
        p.clicar(self, "id", v.btnNove)

        d.gerarScreenshot(self, dirSubtracao, "Ev1")
        sleep(1)

        p.clicar(self,"id",v.btnSubtrair)

        p.clicar(self, "id", v.btnQuatro)
        p.clicar(self, "id", v.btnCinco)
        p.clicar(self, "id", v.btnSeis)

        d.gerarScreenshot(self, dirSubtracao, "Ev2")
        sleep(1)

        p.clicar(self, "id", v.btnIgual)

        d.gerarScreenshot(self, dirSubtracao, "Ev3")
        p.validarTexto(self, "id", v.txtResultado, "123")
        sleep(1)

        p.clicar(self, "id", v.btnC)
        d.criarDocumentoDeEvidencia(self, dirSubtracao, "CT02", "Cálculo Subtracao Android")

    def multiplicao(self):
        d.criarPastaEvidencia(self, dirMultiplicacao)
        p.clicar(self, "id", v.btnC)

        p.clicar(self, "id", v.btnTres)
        p.clicar(self, "id", v.btnUm)

        sleep(1)
        d.gerarScreenshot(self, dirMultiplicacao, "Ev1")
        p.clicar(self, "id", v.btnMultiplicar)

        p.clicar(self, "id", v.btnUm)
        p.clicar(self, "id", v.btnZero)

        d.gerarScreenshot(self, dirMultiplicacao, "Ev2")

        p.clicar(self, "id", v.btnIgual)
        sleep(1)
        d.gerarScreenshot(self, dirMultiplicacao, "Ev3")
        p.validarTexto(self, "id", v.txtResultado, "310")
        sleep(1)

        p.clicar(self, "id", v.btnC)
        d.criarDocumentoDeEvidencia(self, dirMultiplicacao, "CT03", "Cálculo Multiplicacao Android")

    def divisao(self):
        d.criarPastaEvidencia(self, dirDivisao)
        p.clicar(self, "id", v.btnC)

        p.clicar(self, "id", v.btnNove)
        p.clicar(self, "id", v.btnZero)
        p.clicar(self, "id", v.btnZero)

        p.clicar(self, "id", v.btnDivisao)

        p.clicar(self, "id", v.btnZero)

        p.validarTexto(self,"id",v.txtResultado,"0")
        sleep(1)
        p.clicar(self, "id", v.btnC)

        p.clicar(self, "id", v.btnNove)
        p.clicar(self, "id", v.btnZero)
        p.clicar(self, "id", v.btnZero)

        d.gerarScreenshot(self, dirDivisao, "Ev1")
        p.clicar(self, "id", v.btnDivisao)

        p.clicar(self, "id", v.btnQuatro)

        d.gerarScreenshot(self, dirDivisao, "Ev2")

        p.clicar(self, "id", v.btnIgual)
        sleep(1)
        d.gerarScreenshot(self, dirDivisao, "Ev3")
        p.validarTexto(self, "id", v.txtResultado, "225")
        sleep(1)

        p.clicar(self, "id", v.btnC)
        d.criarDocumentoDeEvidencia(self, dirDivisao, "CT04", "Cálculo Divisao Android")