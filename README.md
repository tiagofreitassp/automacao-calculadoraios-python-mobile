# automacao-calculadoraandroid-python-mobile
Script para teste automatizado para calculos simples na Calculadora no iOS usando Python, Appium e Unittest.

### Cobertura dos testes:  ###

* Realizar calculos basicos na calculadora do iOS no emulador.
*
Realizar calculos basicos na calculadora do iOS no smartphone.

## Tecnologias:
* [Python 3.8](https://www.python.org/)
* [Unittest](https://docs.python.org/3/library/unittest.html)
* [Selenium](https://selenium-python.readthedocs.io/)
* [Pycharm](https://www.jetbrains.com/pt-br/pycharm/)
* [PyPI](https://pypi.org/project/selenium/)

## Dependências:
* Selenium
* OS
* Appium-Python-Client
* Time
* DocX
* Utilize o pip install para instalar via terminal os drivers dos navegadores.

## Instruções de execução:

###  - App
*Importante:

O app da calculadora do iOS utilizado para o teste deste projeto foi desenvolvido por terceiro e não por mim, caso execute com sucesso ou não, recomendo que após entender o código escrito, instale outro arquivo do formato .ipa e adapte o projeto. 

Mas deixei o codigo fonte (SimpleCalculator-master.zip) na pasta drivers/iOS caso tenha problemas com o BundleId, abra o codigo fonte e altere o BundleId na sua conta Apple ID.

Antes de executar, espero que saiba de instruções sobre o Apple ID, WebDriverAgent, Node, Appium e dependencias no MacOS, são exigências para automação nas plataformas da Apple.

###  - Plataforma
*Importante:

O projeto foi criado para executar no MacOS. Mas pode receber adaptacoes para executar no Windows e Linux caso nao execute bem fora do MacOS.

Recomendado utilizar o PyCharm, mas pode usar o Eclipse IDE ou Visual Studio Code.

###  - Fluxo
*Descricao: Este script ira executar uma compra online, seguindo o fluxo desde a escolha do produto ate a etapa de confirmacao da compra.

###  - Massas
*Descricao: 
Nao e necessario criar massas por enquanto.

###  - Evidencias
*Descricao:
Apos a execucao as imagens de evidencias sao armazenadas na pasta evidencias.

Para visualizar as evidencias no documento pode usar o MS Office Word ou o LibreOffice

###  - Inicializar a automação
*Descricao:

Para executar num smartphone/simulador, abra a classe Mobile Driver e altere os valores das variáveis