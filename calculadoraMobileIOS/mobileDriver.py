import os, shutil
from time import sleep
from appium import webdriver

dir = '../evidencias/'

xcodeOrgId = "3P3JYXL37U"
xcodeSigningId = "iPhone 8 Plus"
udid = "1ac1b2904df1922053361fdb6b3044d649e3d5fd"
platformName = "iOS"
deviceName = "TF"
platformVersion = "13.5"
bundleId = "com.TiagoFreitas.SimpleCalculator"
automationName = "XCUITest"
driverApp = "/Users/user/Documents/Scripts programacao/XcodeProjects/Apps/SimpleCalculator.ipa"

class mobileDriver():
    def criarPastaEvidencia(self, nPasta):
            d = nPasta
            if os.path.exists(d) == True:
                print("Diretório já existe")
                #os.rmdir(d)
                shutil.rmtree(d)
                print('Diretório apagado')
                os.makedirs(d)
                print('Diretório recriado')
            else:
                print("Diretório não existe")
                os.makedirs(d)
                print('Diretório criado')

    def gerarScreenshot(self, nPasta, nEvidencia):
        sleep(1)
        self.driver.get_screenshot_as_file(nPasta + "/" + nEvidencia + ".png")

    def criarDriver(self):
        desired_caps = {}
        desired_caps['platformName'] = platformName
        desired_caps['deviceName'] = deviceName
        desired_caps['automationName'] = automationName
        #desired_caps['xcodeOrgId'] = xcodeOrgId
        desired_caps['xcodeSigningId'] = xcodeSigningId
        desired_caps['udid'] = udid
        desired_caps['platformVersion'] = platformVersion
        desired_caps['bundleId'] = bundleId
        desired_caps['app'] = driverApp
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(12)

    def fecharDriver(self):
        self.driver.quit()