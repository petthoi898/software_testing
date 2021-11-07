from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from ddt import ddt, data, unpack
import csv        


import unittest


login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[5]/div/div/div/a"
test_forum_xpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a"
create_new_topic_xpath = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/div[2]/a"

def get_csv_data(csv_path):
    """
    read test data from csv and return as list

    @type csv_path: string
    @param csv_path: some csv path string
    @return list
    """
    rows = []
    csv_data = open(str(csv_path), "r")
    content = csv.reader(csv_data)

    # skip header line
    next(content, None)

    # add rows to list
    for row in content:
        rows.append(row)

    return rows

@ddt
class CreateTopicTest(unittest.TestCase):
    # @classmethod
    def setUp(self):
        # with webdriver.Chrome(executable_path='/home/c45/Desktop/testing/chromedriver') as driver:
        self.pathchromeDriver = '/home/c45/Desktop/testing/chromedriver' #path to chrome driver
        self.driver = webdriver.Chrome(executable_path = self.pathchromeDriver)
        self.username=""
        self.password=""
        with open("credential_file.txt","r") as f: 
            self.username = f.readline().strip()
            self.password = f.readline().strip()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://e-learning.hcmut.edu.vn/login/")
        self.driver.find_element(By.XPATH, login_button_xpath).click()
        # fill in credentials
        self.driver.find_element(By.ID, "username").send_keys(self.username)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        # Click Login Button 
        self.driver.find_element(By.NAME,"submit").click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()    
        WebDriverWait(self.driver,timeout=20).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
        self.driver.find_element(By.XPATH, software_testing_course_link_xpath).click()


        WebDriverWait(self.driver,timeout=20).until(lambda d: d.find_element(By.XPATH, test_forum_xpath))
        self.driver.find_element(By.XPATH, test_forum_xpath).click()

        #get in page create new topic
        WebDriverWait(self.driver,timeout=20).until(lambda d: d.find_element(By.XPATH, create_new_topic_xpath))
        self.driver.find_element(By.XPATH, create_new_topic_xpath).click()

        
        # first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
        # print(first_result.get_attribute("textContent"))
        # assert(first_result.get_attribute("textContent") == "Cheese - asdfsdafWikipedia")
    
    @data(*get_csv_data('./test_topic.csv'))
    @unpack
    def test_normalflow(self, subject, message, expected_subject, expected_message):
        #fill in subject and message
        self.driver.find_element(By.ID, "id_subject").send_keys(subject)
        self.driver.find_element(By.ID, "id_messageeditable").send_keys(message)

        #click submit
        self.driver.find_element(By.ID,"id_submitbutton").click()

        #get data from new topic
        new_topic_full_xpath = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a"
        newsubject_full_xpath = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/header/div[2]/h3"
        newmessage_full_xpath = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div/div[2]/div[1]"
        WebDriverWait(self.driver,timeout=20).until(lambda d: d.find_element(By.XPATH, new_topic_full_xpath))
        self.driver.find_element(By.XPATH, new_topic_full_xpath).click()
        WebDriverWait(self.driver,timeout=20).until(lambda d: d.find_element(By.XPATH, newsubject_full_xpath))
        WebDriverWait(self.driver,timeout=20).until(lambda d: d.find_element(By.XPATH, newmessage_full_xpath))
        new_subject = self.driver.find_element(By.XPATH, newsubject_full_xpath).text
        new_message = self.driver.find_element(By.XPATH, newmessage_full_xpath).text

        #check result
        self.assertTrue(subject == expected_subject and message == expected_message)


    def test_exceptionflow_nosubject(self):
        #don't fill in subject
        subject="test"
        message="ping pong\nping pong "
        #self.driver.find_element(By.ID, "id_subject").send_keys(subject)
        self.driver.find_element(By.ID, "id_messageeditable").send_keys(message)

        #click submit
        self.driver.find_element(By.ID,"id_submitbutton").click()

        #error pop up
        result = True
        try:
            self.driver.implicitly_wait(5000)
            self.driver.find_element(By.ID, 'id_error_subject')
        except NoSuchElementException:
            result = False
        self.assertTrue(result)

    def test_exceptionflow_nomessage(self):
        #don't fill in message
        subject="test"
        message="ping pong\nping pong "
        self.driver.find_element(By.ID, "id_subject").send_keys(subject)
        #self.driver.find_element(By.ID, "id_messageeditable").send_keys(message)

        #click submit
        self.driver.find_element(By.ID,"id_submitbutton").click()

        #error pop up
        result = True
        try:
            self.driver.implicitly_wait(5000)
            self.driver.find_element(By.ID, 'id_error_message')
        except NoSuchElementException:
            result = False
        self.assertTrue(result)

    
    def test_exceptionflow_noboth(self):
        #don't fill in message and subject
        subject="test"
        message="ping pong\nping pong "
        #self.driver.find_element(By.ID, "id_subject").send_keys(subject)
        #self.driver.find_element(By.ID, "id_messageeditable").send_keys(message)

        #can't click the button submit
        result = False
        try:
            #click submit
            self.driver.find_element(By.ID,"id_submitbutton").click()
        except ElementNotInteractableException:
            result = True
        self.assertTrue(result)


    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)


    


  