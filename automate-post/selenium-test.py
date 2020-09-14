from selenium import webdriver
from datetime import timedelta
from user_info_screen import SimpleScreen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def formatVideoDuration(videoDuration):
    hourPlaces = "" if len(videoDuration) > 5 else "00:"
    videoDuration = f"{hourPlaces}{videoDuration}"
    return videoDuration.split(':')[::-1]


def clickBySelector(selector, seconds=1):
    sleep(seconds)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    element.click()


def getAllElementsByClassName(className, seconds=1):
    sleep(seconds)
    return wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, className)))


def getElementByID(elementID, seconds=1):
    sleep(seconds)
    return wait.until(EC.presence_of_element_located((By.ID, elementID)))


def getElementTextBySelector(selector, seconds=1):
    sleep(seconds)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).text


def sendTextOnElementById(elementID, text):
    driver.find_element_by_id(elementID).clear()
    driver.find_element_by_id(elementID).send_keys(text)


def createChromeInstanceWithAddBlock():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension(r"C:\Projects\Python\adblock.crx")
    return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


screen = SimpleScreen()
videoURL, email, password, option = screen.openScreen()
screen.closeWindow()

driver = createChromeInstanceWithAddBlock()
url = videoURL
driver.get(url)
wait = WebDriverWait(driver, 10)

videoTitle = getElementTextBySelector("h1.title.style-scope.ytd-video-primary-info-renderer")
videoDuration = getElementTextBySelector("span.ytp-time-duration")

driver.get("https://aprovadoapp.com/#")

clickBySelector("a.btn.btn-link.dropdown-toggle")

sendTextOnElementById('email', email)
sendTextOnElementById('senha', password)
clickBySelector(".btn.btn-success.btnLogin.__tab-campo")

clickBySelector("ul.nav > li:nth-child(3)")  # Atividades
clickBySelector("button.btn.btn-info.__tab-campo")  # Cadastrar Nova Atividade
clickBySelector("div.btn-group > button")  # Escolher Materia
clickBySelector("ul.dropdown-menu.dropMateria.__tab-campo > li:nth-child(4)")

# Escolher Conteudo
clickBySelector("div.control-group:nth-child(3) > div.controls > div.btn-group > button")
clickBySelector(option)

hora, minuto, segundo = getAllElementsByClassName("input.formDuracao")
splitSegundo, splitMinuto, splitHora = formatVideoDuration(videoDuration)
hora.send_keys(splitHora)
minuto.send_keys(splitMinuto)
segundo.send_keys(splitSegundo)

anotacoes = getElementByID("__atividade-cadasteditar-anotacoes")
anotacoes.send_keys(videoTitle)
clickBySelector("button.btn.btn-success.__tab-campo")
sleep(2)
driver.quit()
