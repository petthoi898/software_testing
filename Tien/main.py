from re import S
import time
import unittest
import chromedriver_autoinstaller
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium import webdriver


data = [ "Hai người bị cách chức tất cả các chức vụ trong Đảng gồm ông Nguyễn Minh Tuấn, Bí thư Chi bộ, Vụ trưởng Vụ Trang thiết bị và Công trình y tế; Nguyễn Chiến Thắng, nguyên Bí thư Chi bộ, nguyên Giám đốc Ban Quản lý dự án công trình y tế trọng điểm kiêm Giám đốc Ban Quản lý dự án chuyên ngành xây dựng công trình y tế, Bộ Y tế. Bốn người khác bị khiển trách gồm ông Nguyễn Trường Sơn, Ủy viên Ban cán sự đảng, Thứ trưởng Bộ Y tế; Nguyễn Thế Thịnh, Bí thư Chi bộ, Cục trưởng Cục Quản lý Y, Dược cổ truyền; Vũ Tuấn Cường, Đảng ủy viên Bộ Y tế, Bí thư Đảng ủy, Cục trưởng Cục Quản lý Dược; Nguyễn Trí Dũng, Bí thư Chi bộ, Giám đốc Trung tâm mua sắm tập trung thuốc Quốc gia.UBKT Trung ương cho biết sẽ tiếp tục xem xét, xử lý kỷ luật một số tổ chức đảng và đảng viên có liên quan đến vi phạm, khuyết điểm đã nêu; đồng thời, yêu cầu Ban cán sự đảng, Ban Thường vụ Đảng ủy Bộ Y tế chỉ đạo khắc phục các vi phạm, khuyết điểm, kiểm điểm trách nhiệm và xử lý kỷ luật đối với các tổ chức đảng, đảng viên khác có liên quan."
    ,"Ngoài đề nghị Bộ Chính trị, Ban Bí thư xem xét kỷ luật hai cá nhân nêu trên, Ủy ban Kiểm tra Trung ương đã quyết định cảnh cáo Ban Thường vụ Đảng ủy Bộ Y tế nhiệm kỳ 2015-2020, Đảng ủy Cục Quản lý Dược nhiệm kỳ 2010-2015, Ban Thường vụ Đảng ủy Bệnh viện Bạch Mai nhiệm kỳ 2015-2020; Khiển trách Đảng ủy Cục Quản lý Dược nhiệm kỳ 2015-2020."
    , "Ủy ban Kiểm tra Trung ương đánh giá, những vi phạm nêu trên đã gây hậu quả nghiêm trọng, thất thoát, lãng phí tiền, tài sản của Nhà nước, thiệt hại cho Quỹ Bảo hiểm y tế, ảnh hưởng lớn đến chủ trương của Đảng, chính sách, pháp luật của Nhà nước về bảo vệ và"
]

class Test(unittest.TestCase):
    def testEditComment(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        firstPost = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[8]/th/div/a"
        #comment =       "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div[1]/div[2]/div[2]/div/a[4]"
        postComment =    "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div[2]/div/form/div[2]/button[1]/span[1]"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
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
            #WebDriverWait(driver, 100)
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click()
            driver.find_element(By.XPATH, firstPost).click()  #click to a post  
            time.sleep(2)
            driver.find_element(By.LINK_TEXT, 'Trả lời').click()   #click to comment
            time.sleep(3)
            driver.find_element(By.NAME, 'post').send_keys(data)
            driver.find_element(By.XPATH, postComment).click()
            time.sleep(4)
            #post = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]")
            driver.find_element(By.LINK_TEXT, 'Chỉnh sửa').click()
            time.sleep(5)
            editXpath = "/html/body/div[2]/div[3]/div/div/section/div[1]/form/fieldset/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div"
            edit = driver.find_element(By.XPATH, editXpath)
            edit.click()
            edit.send_keys(" edited comment")
            driver.find_element(By.ID, "id_submitbutton").click()
            self.assertTrue(True)
    
    def testDeleteComment(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        firstPost = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[8]/th/div/a"
        postComment =    "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div[2]/div/form/div[2]/button[1]/span[1]"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
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
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click()
            driver.find_element(By.XPATH, firstPost).click()  #click to a post  
            time.sleep(2)
            driver.find_element(By.LINK_TEXT, 'Trả lời').click()   #click to comment
            time.sleep(3)
            driver.find_element(By.NAME, 'post').send_keys("This is first comment")
            driver.find_element(By.XPATH, postComment).click()
            time.sleep(4)
            #count number of comment before del
            post = driver.find_element(By.CLASS_NAME, 'indent')
            allCommentBefore = post.find_elements(By.TAG_NAME, 'article')
            countBefore = len(allCommentBefore)
            driver.find_element(By.LINK_TEXT, 'Xóa').click()
            time.sleep(3)
            acpXpath = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/div/div[3]/div/div[1]"
            driver.find_element(By.XPATH, acpXpath).click()
            time.sleep(3)
            #count number of comment after del
            postNew = driver.find_element(By.CLASS_NAME, 'indent')
            allCommentAfter = postNew.find_elements(By.TAG_NAME, 'article')
            countAfter = len(allCommentAfter)
            #checking 
            self.assertTrue(countBefore - 1 == countAfter)
            self.assertFalse(countBefore - 1 != countAfter)


    def testComment(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        firstPost = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a"
        comment =       "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div/div[2]/div[2]/div/a[2]"
        postComment =    "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div[2]/div/form/div[2]/button[1]/span[1]"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
            username=""
            password=""
            with open("credential_file.txt","r") as f: 
                username = f.readline().strip()
                password = f.readline().strip()
            print(f"username is: {username}|{password}")
            wait = WebDriverWait(driver, 10)
            driver.get("http://e-learning.hcmut.edu.vn/login/")
            driver.find_element(By.XPATH, login_button_xpath).click()
            # fill in credentials
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            # Click Login Button 
            driver.find_element(By.NAME,"submit").click()
            #WebDriverWait(driver, 100)
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click()
            driver.find_element(By.XPATH, firstPost).click()  #click to a post  
            driver.find_element(By.XPATH, comment).click()   #click to comment
            time.sleep(3)
            #driver.find_element(By.XPATH, inputComment).click()\
            post = driver.find_element(By.CLASS_NAME, 'indent')
            allCommentBefore = post.find_elements(By.TAG_NAME, 'article')
            countBefore = len(allCommentBefore)
            print(countBefore)
            driver.find_element(By.NAME, 'post').send_keys("This is test from Selenium")
            driver.find_element(By.XPATH, postComment).click()
            time.sleep(5)
            allCommentAfter = post.find_elements(By.TAG_NAME, 'article')
            countAfter = len(allCommentAfter)
            print(len(allCommentAfter))
            self.assertTrue(countBefore + 1 == countAfter)
            self.assertFalse(countBefore + 1!= countAfter)
    def testCommentDDT(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        firstPost = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a"
        comment =       "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div/div[2]/div[2]/div/a[2]"
        postComment =    "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div[2]/div/form/div[2]/button[1]/span[1]"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
            username=""
            password=""
            with open("credential_file.txt","r") as f: 
                username = f.readline().strip()
                password = f.readline().strip()
            print(f"username is: {username}|{password}")
            wait = WebDriverWait(driver, 10)
            driver.get("http://e-learning.hcmut.edu.vn/login/")
            driver.find_element(By.XPATH, login_button_xpath).click()
            # fill in credentials
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            # Click Login Button 
            driver.find_element(By.NAME,"submit").click()
            #WebDriverWait(driver, 100)
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click()
            driver.find_element(By.XPATH, firstPost).click()  #click to a post  
            driver.find_element(By.XPATH, comment).click()   #click to comment
            time.sleep(3)
            #driver.find_element(By.XPATH, inputComment).click()\
            post = driver.find_element(By.CLASS_NAME, 'indent')
            allCommentBefore = post.find_elements(By.TAG_NAME, 'article')
            countBefore = len(allCommentBefore)
            print(countBefore)
            driver.find_element(By.NAME, 'post').send_keys(data[0])
            driver.find_element(By.XPATH, postComment).click()
            time.sleep(5)
            allCommentAfter = post.find_elements(By.TAG_NAME, 'article')
            countAfter = len(allCommentAfter)
            print(len(allCommentAfter))
            self.assertTrue(countBefore + 1 == countAfter)
            self.assertFalse(countBefore + 1!= countAfter)
    def testCommentDDT1(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        firstPost = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a"
        comment =       "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div/div[2]/div[2]/div/a[2]"
        postComment =    "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div[2]/div/form/div[2]/button[1]/span[1]"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
            username=""
            password=""
            with open("credential_file.txt","r") as f: 
                username = f.readline().strip()
                password = f.readline().strip()
            print(f"username is: {username}|{password}")
            wait = WebDriverWait(driver, 10)
            driver.get("http://e-learning.hcmut.edu.vn/login/")
            driver.find_element(By.XPATH, login_button_xpath).click()
            # fill in credentials
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            # Click Login Button 
            driver.find_element(By.NAME,"submit").click()
            #WebDriverWait(driver, 100)
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click()
            driver.find_element(By.XPATH, firstPost).click()  #click to a post  
            driver.find_element(By.XPATH, comment).click()   #click to comment
            time.sleep(3)
            #driver.find_element(By.XPATH, inputComment).click()\
            post = driver.find_element(By.CLASS_NAME, 'indent')
            allCommentBefore = post.find_elements(By.TAG_NAME, 'article')
            countBefore = len(allCommentBefore)
            print(countBefore)
            driver.find_element(By.NAME, 'post').send_keys(data[1])
            driver.find_element(By.XPATH, postComment).click()
            time.sleep(5)
            allCommentAfter = post.find_elements(By.TAG_NAME, 'article')
            countAfter = len(allCommentAfter)
            print(len(allCommentAfter))
            self.assertTrue(countBefore + 1 == countAfter)
            self.assertFalse(countBefore + 1!= countAfter)
    def testCommentDDT2(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        firstPost = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a"
        comment =       "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div/div[2]/div[2]/div/a[2]"
        postComment =    "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div[2]/div/form/div[2]/button[1]/span[1]"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
            username=""
            password=""
            with open("credential_file.txt","r") as f: 
                username = f.readline().strip()
                password = f.readline().strip()
            print(f"username is: {username}|{password}")
            wait = WebDriverWait(driver, 10)
            driver.get("http://e-learning.hcmut.edu.vn/login/")
            driver.find_element(By.XPATH, login_button_xpath).click()
            # fill in credentials
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            # Click Login Button 
            driver.find_element(By.NAME,"submit").click()
            #WebDriverWait(driver, 100)
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click()
            driver.find_element(By.XPATH, firstPost).click()  #click to a post  
            driver.find_element(By.XPATH, comment).click()   #click to comment
            time.sleep(3)
            #driver.find_element(By.XPATH, inputComment).click()\
            post = driver.find_element(By.CLASS_NAME, 'indent')
            allCommentBefore = post.find_elements(By.TAG_NAME, 'article')
            countBefore = len(allCommentBefore)
            print(countBefore)
            driver.find_element(By.NAME, 'post').send_keys(data[2])
            driver.find_element(By.XPATH, postComment).click()
            time.sleep(5)
            allCommentAfter = post.find_elements(By.TAG_NAME, 'article')
            countAfter = len(allCommentAfter)
            print(len(allCommentAfter))
            self.assertTrue(countBefore + 1 == countAfter)
            self.assertFalse(countBefore + 1!= countAfter)
    def testFollow(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
            username=""
            password=""
            with open("credential_file.txt","r") as f: 
                username = f.readline().strip()
                password = f.readline().strip()
            print(f"username is: {username}|{password}")
            wait = WebDriverWait(driver, 10)
            driver.get("http://e-learning.hcmut.edu.vn/login/")
            driver.find_element(By.XPATH, login_button_xpath).click()
            # fill in credentials
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            # Click Login Button 
            driver.find_element(By.NAME,"submit").click()
            #WebDriverWait(driver, 100)
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click() # click to forum
            followButton = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[6]/div/input"
            check = driver.find_element(By.XPATH, followButton).is_selected()
            time.sleep(2)
            xp = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[6]"
            if check:
                driver.find_element(By.XPATH, xp).click()
            driver.find_element(By.XPATH, xp).click()
            check = driver.find_element(By.XPATH, followButton).is_selected()
            self.assertTrue(check == True)
            self.assertFalse(check == False)
            
    def testUnfollow(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
            username=""
            password=""
            with open("credential_file.txt","r") as f: 
                username = f.readline().strip()
                password = f.readline().strip()
            print(f"username is: {username}|{password}")
            wait = WebDriverWait(driver, 10)
            driver.get("http://e-learning.hcmut.edu.vn/login/")
            driver.find_element(By.XPATH, login_button_xpath).click()
            # fill in credentials
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            # Click Login Button 
            driver.find_element(By.NAME,"submit").click()
            #WebDriverWait(driver, 100)
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click() # click to forum
            followButton = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[6]/div/input"
            check = driver.find_element(By.XPATH, followButton).is_selected()
            xp = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[6]"
            if not check:
                driver.find_element(By.XPATH, xp).click()
            driver.find_element(By.XPATH, xp)
            check =  driver.find_element(By.XPATH, xp).is_selected()
            self.assertTrue(check == False)
            self.assertFalse(check == True)
    

    def testBookMark(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
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
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click()
            #driver.find_element(By.XPATH, firstPost).click()  #click to a post  
            #infor bookmark
            bookmarkPath = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a"
            nameOfBookmark = driver.find_element(By.XPATH, bookmarkPath).text
            starBookmark = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[1]/a"
            driver.find_element(By.XPATH, starBookmark).click()
            time.sleep(3)
            driver.refresh()
            #/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div
            #/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a
            nameAfterXpath = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a"
            nameAfter = driver.find_element(By.XPATH, nameAfterXpath).text
            self.assertTrue(nameOfBookmark == nameAfter)
            self.assertFalse(nameOfBookmark != nameAfter)
    def testSort(self):
        login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
        software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[8]/div/div/div/a"
        forumXpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a/span"
        chromedriver_autoinstaller.install()
        with webdriver.Chrome() as driver:
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
            # fault for exception
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "closebutton"))).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
            driver.find_element(By.XPATH, software_testing_course_link_xpath).click()
            WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, forumXpath))
            driver.find_element(By.XPATH, forumXpath).click()
            time.sleep(2)
            driver.find_element(By.NAME, 'group').click()
            selectGroup = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/div[1]/div/form/select/optgroup[1]/option[1]"
            driver.find_element(By.XPATH, selectGroup).click()
            self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()