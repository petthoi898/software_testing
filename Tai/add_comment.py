from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException      
from selenium.common.exceptions import TimeoutException
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
class AddCommentTest(unittest.TestCase):
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

        #get in a topic
        new_topic_full_xpath = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a"
        WebDriverWait(self.driver,timeout=20).until(lambda d: d.find_element(By.XPATH, new_topic_full_xpath))
        self.driver.find_element(By.XPATH, new_topic_full_xpath).click()

        #get in box add comment
        add_comment_full_xpath = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div/div[2]/div[2]/div/a[2]"
        WebDriverWait(self.driver,timeout=20).until(lambda d: d.find_element(By.XPATH, add_comment_full_xpath))
        self.driver.find_element(By.XPATH, add_comment_full_xpath).click()

        
    @data(*get_csv_data('./test_comment.csv'))
    @unpack
    def test_normalflow(self, content, expected_result):
        #fill in comment

        input_content_full_xpath = "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div[2]/div/form/div[1]/span/textarea"
        WebDriverWait(self.driver,timeout=10).until(lambda d: d.find_element(By.XPATH, input_content_full_xpath))
        self.driver.find_element(By.XPATH, input_content_full_xpath).send_keys(content)

        #click submit
        submit_button_full_xpath = "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div[2]/div/form/div[2]/button[1]"
        WebDriverWait(self.driver,timeout=10).until(lambda d: d.find_element(By.XPATH, submit_button_full_xpath))
        self.driver.find_element(By.XPATH,submit_button_full_xpath).click()

        # comment_xpath = '/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[2]/article[3]/div[1]/div/div/div[2]/div[1]/div'
        # WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, comment_xpath))
        # print(f"{self.driver.find_element(By.XPATH, comment_xpath).text}\n")

        #find biggest num comment
        i = 0
        try:
            while (True):
                i+=1
                temp_comment_xpath = '/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[2]/article[' + str(i) + ']/div[1]/div/div/div[2]/div[1]/div'
                WebDriverWait(self.driver,timeout=5).until(lambda d: d.find_element(By.XPATH, temp_comment_xpath))
        except TimeoutException:
            i-=1
            final_comment_xpath = '/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[2]/article[' + str(i) + ']/div[1]/div/div/div[2]/div[1]/div'
            new_content = self.driver.find_element(By.XPATH,final_comment_xpath).text
            self.assertTrue(new_content == expected_result)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)


    


  