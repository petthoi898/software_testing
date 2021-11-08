from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC

login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
software_testing_course_link_xpath = "//*[@id='page-container-2']/div/ul/ul[1]/li[6]/div/div/div/a"
test_forum_xpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a"
topic = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a"

def login(driver):
    username=""
    password=""
    with open("credential_file.txt","r") as f: 
        username = f.readline().strip()
        password = f.readline().strip()
    
    wait = WebDriverWait(driver, 10)
    driver.get("http://e-learning.hcmut.edu.vn/login/")
    driver.find_element(By.XPATH, login_button_xpath).click()
    # fill in credentials
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    # Click Login Button 
    driver.find_element(By.NAME,"submit").click()

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, software_testing_course_link_xpath))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, test_forum_xpath))).click()
    driver.find_element(By.XPATH, topic).click()