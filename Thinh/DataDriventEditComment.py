from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import unittest
import random
import pytest


@pytest.mark.parametrize('new_message,expected_result',[
    ('Thinh is a God','Thinh is a God'),
    ('God is Thinh','God is Thinh'),
    ('Thinh test','Thinh test'),
    ('A test by thinh','A test by thinh')
])
def testChangePredefinedText(self,new_message,expected_result):
    WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, comment_list_container_xpath))
    replies_container = self.driver.find_element(By.XPATH,comment_list_container_xpath)
    replies_container.find_element(By.XPATH,f'div[{self.comments_num}]/a[1]').click() 
    WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, new_comment_edit_xpath))
    self.driver.find_element(By.XPATH,new_comment_edit_xpath).click()
    self.driver.save_screenshot(f'image.png') 
    WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, new_comment_title_xpath))
    edit_box = self.driver.find_element(By.XPATH,new_comment_edit_box_xpath)
    if self.debug:
        print("TESTING WITH MESSAGE: ",new_message)
    # Focus the box 
    edit_box.click() 
    # Clear the current content 
    webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform() 
    # Enter the new message 
    edit_box.send_keys(new_message)
    # Submit edit 
    self.submit_edit(); 
    # Go back to the editted comment 
    new_comment = self.findNewlyEditedComment() 
    new_comment.click() 
    new_comment_content_xpath = '/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div/div[2]/div[1]'

    WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH,new_comment_content_xpath))

    # Check if the message is edited 
    new_comment_content = self.driver.find_element(By.XPATH,new_comment_content_xpath).get_attribute('innerText')
    if self.debug: 
        print(f"Entered Message is: {new_message}\nFound Message is: {new_comment_content}")
    self.assertEqual(new_comment_content.strip(),expected_result)
    self.driver.back()
    self.driver.save_screenshot('./image.png')
