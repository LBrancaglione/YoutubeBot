import chromedriver_binary
from selenium import webdriver
import time


class RoboYoutube:
    def __init__(self):
        self.webdriver = webdriver.Chrome()

    def busca(self, busca, paginas):
        videos = []
        pagina = 1

        url = "https://www.youtube.com/results?search_query=%s" % busca
        self.webdriver.get(url)
        while pagina <= paginas:
            titulos = self.webdriver.find_elements("xpath", "//a[@id='video-title']")
            for titulo in titulos:
                if titulo.text not in videos:
                    print("Video encontrado: %s" % titulo.text)
                    videos.append(titulo.text)
            self.proxima_pagina(pagina)
            pagina += 1

    def proxima_pagina(self, pagina):
        print("mudando para %s" % (pagina + 1))
        bottom = pagina * 10000
        self.webdriver.execute_script("window.scrollTo(0, %s);" % bottom)
        time.sleep(5)
        pass


bot = RoboYoutube()
bot.busca("minecraft", 5)
