from os import remove
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
unittest.TestLoader.sortTestMethodsUsing = None

from Util import login

PATH = "C:\Program Files (x86)\chromedriver.exe"

class ReplyComment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver_wait = WebDriverWait(self.driver, 10)
        # login
        login(self.driver)

    def test_reply_comment(self):
        driver = self.driver
        driver_wait = self.driver_wait

        ##comment
        button_setting = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/div[1]/div/div/div/a"
        driver.find_element(By.XPATH, button_setting).click()

        button_subscribe = "/html/body/div[2]/div[3]/div/div/section/div[1]/div/div[1]/div/div/div/div/a[2]"
        WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, button_subscribe))
        driver.find_element(By.XPATH, button_subscribe).click()

if __name__ == "__main__":
    unittest.main()
  
  