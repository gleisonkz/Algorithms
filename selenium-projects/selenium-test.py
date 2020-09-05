from selenium import webdriver
from datetime import datetime
from datetime import timedelta
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def convertStringTimeToSeconds(string):
    timeSplit = map(int, string.split(':')[::-1])
    seconds = 0
    for index, item in enumerate(timeSplit):
        dic = [item, item * 60, item * 3600]
        seconds = seconds + dic[index]
    return seconds

def clickBySelector(selector, seconds=1):
    sleep(seconds)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, f"{selector}"))).click()

def getAllElementsByClassName(className,seconds=1):
    sleep(seconds)
    return wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, className)))

def getElementByID(elementID,seconds=1):
    sleep(seconds)
    return wait.until(EC.presence_of_element_located(
        (By.ID, elementID)))

def getElementTextBySelector(selector,seconds=1):
    sleep(seconds)
    return wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, selector))).text

def sendTextOnElementById(elementID,text):
    driver.find_element_by_id(elementID).clear()
    driver.find_element_by_id(elementID).send_keys(text) 

def createChromeInstanceWithAddBlock():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension(r"C:\Projects\Python\adblock.crx")
    return webdriver.Chrome(ChromeDriverManager().install(), options= chrome_options)

driver = createChromeInstanceWithAddBlock()
url = "https://www.youtube.com/watch?v=O_sIPPA4euw&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=6"
driver.get(url)
wait = WebDriverWait(driver, 10)

videoTitle = getElementTextBySelector("h1.title.style-scope.ytd-video-primary-info-renderer")    
videoDuration = getElementTextBySelector("span.ytp-time-duration")    
teste = convertStringTimeToSeconds(videoDuration)
novoTime = str(timedelta(seconds=teste))

driver.get("https://aprovadoapp.com/#")

clickBySelector("a.btn.btn-link.dropdown-toggle")

sendTextOnElementById('email','gleisonsubzerokz@gmail.com')
sendTextOnElementById('senha','g33888705')
clickBySelector(".btn.btn-success.btnLogin.__tab-campo")

clickBySelector("ul.nav > li:nth-child(3)")
clickBySelector(".icon-plus.icon-white")
clickBySelector("div.btn-group > button")

clickBySelector("ul.dropdown-menu.dropMateria.__tab-campo > li:nth-child(4)")
clickBySelector("div.control-group:nth-child(3) > div.controls > div.btn-group > button")# Passive Listening
clickBySelector("ul.nav.nav-list.conteudoItemLista.__tab-campo > li:nth-child(2)")

hora, minuto, segundo = getAllElementsByClassName("input.formDuracao")
splitHora, splitMinuto, splitSegundo = map(int, novoTime.split(":"))
hora.send_keys(splitHora)
minuto.send_keys(splitMinuto)
segundo.send_keys(splitSegundo)

anotacoes = getElementByID("__atividade-cadasteditar-anotacoes")
anotacoes.send_keys(videoTitle)
stop = "stop"
clickBySelector("button.btn.btn-success.__tab-campo")
