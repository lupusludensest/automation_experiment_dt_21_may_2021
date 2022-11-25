from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Screenshot import Screenshot_Clipping
import time

# Locators
SRCH_FLD = (By.XPATH, "//input[@class='gh-tb ui-autocomplete-input']")
SRCH_BTN = (By.XPATH, "//input[@class = 'btn btn-prim gh-spr']")
XPCTD_MSG = (By.XPATH, "(//*[contains(text(),'Clothing, Shoes & Accessories')])[2]")
IFRMS = (By.TAG_NAME, 'iframe')

class MainPage(Page):

    # 1 Go to main page send search ford to field and verify respond is expected
    def snd_wrd(self, shs):
        self.input_text(shs, *SRCH_FLD)

    def clck_srch_btn(self):
        self.click(*SRCH_BTN)

    def vrfctn_hr(self, vrfctn_hr):
        self.verify_text(vrfctn_hr, *XPCTD_MSG)

    def find_iframes(self):
        self.find_elements(*IFRMS)
        print(f'Number of iframes: {len(IFRMS)}; type of iframes: {type(IFRMS)}')
        print(f'iFrames: {IFRMS}')
    # End of the above code




