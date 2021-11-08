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

        # click button reply comment
        button_reply_comment = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[2]/article[1]/div[1]/div/div/div[2]/div[2]/div/a[3]"
        driver_wait.until(EC.element_to_be_clickable((By.XPATH, button_reply_comment))).click()
        
        # find textarea element
        textarea_xpath = "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[2]/article[1]/div[1]/div/div[2]/div/form/div[1]/span/textarea"
        driver_wait.until(lambda d: d.find_element(By.XPATH, textarea_xpath))
        textarea = driver.find_element(By.XPATH, textarea_xpath)

        # reply comment
        comment = "Some Sample Text Here"
        textarea.send_keys(comment)
        textarea.send_keys(Keys.RETURN)
        
        # submit comment
        button_submit = "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[2]/article[1]/div[1]/div/div[2]/div/form/div[2]/button[1]/span[1]"
        driver.find_element(By.XPATH, button_submit).click()
        
        # get submitted comment
        comment_cur_xpath = "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[2]/article[1]/div[2]/article[last()]/div[1]/div/div/div[2]/div[1]/div"
        submitted_comment = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, comment_cur_xpath)))
        
        self.assertEqual(comment, submitted_comment.text)

    def test_remove_comment(self):
        driver = self.driver
        driver_wait = self.driver_wait
        
        # remove comment
        button_remove_xpath = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[2]/article[1]/div[2]/article[last()]/div[1]/div/div/div[2]/div[2]/div/a[4]"
        driver_wait.until(EC.presence_of_element_located((By.XPATH, button_remove_xpath))).click()

        # confirm remove
        button_confirm_xpath = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/div/div[3]/div/div[1]/form/button"
        confirm_remove = driver_wait.until(EC.element_to_be_clickable((By.XPATH, button_confirm_xpath)))

        try:
            confirm_remove.click()
            isDeleted = True
        except:
            isDeleted = False

        self.assertTrue(isDeleted)

    def test_edit_comment(self):
        driver = self.driver
        driver_wait = self.driver_wait

        # click button edit
        button_edit_xpath = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[2]/article[1]/div[2]/article[last()]/div[1]/div/div/div[2]/div[2]/div/a[3]"
        driver_wait.until(EC.element_to_be_clickable((By.XPATH, button_edit_xpath))).click()

        # get text box element   
        text_box_xpath = "/html/body/div[2]/div[3]/div/div/section/div[1]/form/fieldset/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div"
        text_box = driver_wait.until(EC.presence_of_element_located((By.XPATH, text_box_xpath)))
        text_box.click()
        # remove all current comment
        text_box.send_keys(Keys.CONTROL, 'a')
        text_box.send_keys(Keys.BACK_SPACE)

        new_comment = "change textaaaa"
        # add new comment
        text_box.send_keys(new_comment)
        text_box.send_keys(Keys.RETURN)
        
        # submit new comment
        driver_wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton"))).click()

        # compare with new comment
        new_comment_xpath = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[2]/article[1]/div[2]/article[last()]/div[1]/div/div/div[2]/div[1]/div[1]"
        new_comment_element = driver_wait.until(EC.presence_of_element_located((By.XPATH, new_comment_xpath)))
        self.assertEqual(new_comment_element.text, new_comment)    

if __name__ == "__main__":
    unittest.main()
  
  