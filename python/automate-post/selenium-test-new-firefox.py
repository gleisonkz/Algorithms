from selenium import webdriver
import requests
import PySimpleGUI as sg
import json
from datetime import timedelta
from user_info_screen import SimpleScreen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


def formatVideoDuration(videoDuration: str) -> None:
    hourPlaces = "" if len(videoDuration) > 5 else "00:"
    videoDuration = f"{hourPlaces}{videoDuration}"
    return videoDuration.split(':')


def getSecondsFromStringTime(stringTime: str) -> int:
    """Get Seconds from string time."""
    hour, minutes, seconds = formatVideoDuration(stringTime)
    hour = (int(hour) * 3600)
    minutes = (int(minutes) * 60)
    seconds = int(seconds)
    return (hour + minutes + seconds) * 1000


def getElementTextBySelector(selector, seconds=1) -> str:
    sleep(seconds)
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).text


def createBrowserInstanceWithAddBlock() -> object:
    addBlockFile = r'C:\personal\algorithms-python\automate-post\adblock_plus-3.9.5-an+fx.xpi'
    myOptions = webdriver.FirefoxOptions()
    profile = webdriver.FirefoxProfile()
    # profile.add_extension(r'C:\personal\algorithms-python\automate-post\adblock.crx')
    profile.add_extension(extension=addBlockFile)
    profile.set_preference('extensions.adblockplus.currentVersion', '3.9.5')
    myOptions.headless = False
    myOptions.add_argument("--start-maximized")
    # myOptions.add_extension(r"C:\personal\algorithms-python\automate-post\adblock.crx")
    return webdriver.Firefox(
        executable_path=r'C:\Users\2233\.wdm\drivers\geckodriver\win64\v0.27.0\geckodriver.exe',
        options=myOptions,
        firefox_profile=profile
    )


screen = SimpleScreen()
videoURL, email, password, activityID = screen.openScreen()
screen.closeWindow()


driver = createBrowserInstanceWithAddBlock()
url = videoURL
driver.get(url)
wait = WebDriverWait(driver, 10)

videoTitle = getElementTextBySelector("h1.title.style-scope.ytd-video-primary-info-renderer")
videoDuration = getElementTextBySelector("span.ytp-time-duration")
videoDuration = getSecondsFromStringTime(videoDuration)
driver.quit()


userLogin = {'Email': "gleisonsubzerokz@gmail.com", 'Senha': "g33888705", 'ManterConectado': True}
request = requests.post('https://aprovadoapp.com/service/Usuario/Autenticar', data=userLogin)
headers = {'Content-Type': 'application/json'}
myCookies = request.cookies
myData = {
    "Id": 0,
    "Materia": {
        "Id": 6496550
    },
    "Tipo": "manual",
    "Conteudo": {
        "Id": 9178637
    },
    "DataInicio": "18/09/2020",
    "HoraInicio": "12:13",
    "Anotacoes": f"{videoTitle}",
    "Duracao": videoDuration
}

jsonData = json.dumps(myData)
result = requests.post('https://aprovadoapp.com/service/Atividade/Novo', cookies=myCookies, data=jsonData, headers=headers)
sg.Popup(f"Result Status Code: {result.status_code}")
