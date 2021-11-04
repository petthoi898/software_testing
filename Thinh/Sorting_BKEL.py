from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import unittest

from Util import getCurrentDisccusionList, loginAndGetDiscussionList

STAR_QUOTE = 'Star this discussion'
UNSTAR_QUOTE = 'Unstar this discussion'
#yui_3_17_2_1_1635916493586_512
#yui_3_17_2_1_1635916493586_513

login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[9]/div/div/div/a"
test_forum_xpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a"

first_star_path = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[1]/a"
first_topic_path = "//*[@id='yui_3_17_2_1_1635876930203_521']"
# Discussion List 
disc_list_xpath = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody'

order_title_indicator_path ='/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[2]/span/i'
change_order_title_link_path = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[2]/a'

order_group_indicator_path = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[3]/span/i'
change_order_group_link_path = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[3]/a'

order_created_by_indicator_path = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[4]/span/i'
change_created_by_group_link_path = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[4]/a'
# /html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[5]/a

# /html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[5]/a
order_last_modified_indicator_path = '//html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[5]/span/i'
change_order_last_modified_link_path = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[5]/a'

order_answer_num_indicator_path = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[6]/span/i'
change_order_answer_num_link_path = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/thead/tr/th[6]/a'

ORDER_TITLE_ASC = "Tăng dần"
ORDER_TITLE_DESC = "Giảm dần"

last_topic_anchor = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[7]/td[3]/div/div[2]/div[1]"
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Logger:
    def log_warning(message,value): 
        print(f'{bcolors.WARNING} {message}: {value}')
    def log_grean(message,value):
        print(f'{bcolors.OKGREEN} {message}: {value}')
        
class SortTopicTest(unittest.TestCase):
    @classmethod 
    def setUpClass(inst): 
        # Create a new Firefox session 
        inst.driver = webdriver.Firefox() 
        wait = WebDriverWait(inst.driver, 10) 
        inst.initialTopicList = loginAndGetDiscussionList(inst.driver)
        inst.maxDiff = None

    def getResultAndExpectedByKey(self,key="topic_name",test_ascending=True,print_debug=False):
        if key == 'topic_name': 
            self.indicator_path = order_title_indicator_path
            self.change_order_link_path = change_order_title_link_path
        elif key == 'group_name':
            self.indicator_path  = order_group_indicator_path
            self.change_order_link_path = change_order_group_link_path 
        elif key == 'created_by':
            self.indicator_path  = order_created_by_indicator_path
            self.change_order_link_path = change_created_by_group_link_path
        elif key == 'last_edited_by':
            self.indicator_path  = order_last_modified_indicator_path
            self.change_order_link_path = change_order_last_modified_link_path 
        elif key == 'answer_num':
            self.indicator_path  = order_answer_num_indicator_path
            self.change_order_link_path = change_order_answer_num_link_path
        else: 
            print("INVALID KEY NAME @@")
         
        self.driver.find_element(By.XPATH,self.change_order_link_path).click() 
        WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, last_topic_anchor))
        
        
        self.indicator = self.driver.find_element(By.XPATH,self.indicator_path) 
        self.change_link = self.driver.find_element(By.XPATH,self.change_order_link_path)

        # Then check for desired order
        self.indicator_value = self.indicator.get_attribute('title')
        if test_ascending and self.indicator_value == ORDER_TITLE_DESC:
            self.change_link.click() 
        elif not test_ascending and self.indicator_value == ORDER_TITLE_ASC: 
            self.change_link.click() 
           
        # Researching for the button and indicator 
        WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, first_star_path))   
        # self.driver.implicitly_wait(5) # seconds
        
    
        self.indicator = self.driver.find_element(By.XPATH,self.indicator_path) 
        self.change_link = self.driver.find_element(By.XPATH,self.change_order_link_path)
        # Check the order versus the expected result
        sorted_list = getCurrentDisccusionList(self.driver)
        # Sort the initial list and check 
        initial_list = self.initialTopicList
        expected_sorted_list = sorted(initial_list,key=lambda topic : topic[key],reverse= not test_ascending)
        if print_debug:
            Logger.log_warning(message="\nExpected list is: ", value=expected_sorted_list)
            Logger.log_warning(message="\nResult list is: ", value=sorted_list)
            post_fix = "_asc" if test_ascending else "_desc" 
            self.driver.save_screenshot(f'./{key}{post_fix}.png')

        return [sorted_list,expected_sorted_list]

    def testSortByTopicNameAsc(self): 
        [result,expected] = self.getResultAndExpectedByKey("topic_name",True)
        self.assertListEqual(result,expected)
    
    def testSortByTopicNameDesc(self): 
        [result,expected] = self.getResultAndExpectedByKey("topic_name",False)
        self.assertListEqual(result,expected)

    def testSortByGroupAsc(self): 
        [result,expected] = self.getResultAndExpectedByKey("group_name",False)
        l = map(lambda topic: topic['group_name'],result)
        l = list(l)
        self.assertTrue(sorted(l) == l)
                
    def testSortByGroupDesc(self): 
        [result,expected] = self.getResultAndExpectedByKey("group_name",False)
        l = map(lambda topic: topic['group_name'],result)
        l = list(l)
        self.assertTrue(sorted(l,reverse=True) == l)
        
    def testSortByCreatedAsc(self): 
        [result,expected] = self.getResultAndExpectedByKey("created_by",True)
        l = map(lambda topic: topic['created_by'],result)
        l = list(l)
        self.assertTrue(sorted(l) == l)
        
    def testSortByCreatedDesc(self): 
        [result,expected] = self.getResultAndExpectedByKey("created_by",False)
        l = map(lambda topic: topic['created_by'],result)
        l = list(l)
        self.assertTrue(sorted(l,reverse=True) == l)
        
    def testSortByLastModifiedAsc(self): 
        [result,expected] = self.getResultAndExpectedByKey("last_edited_by",True)
        l = map(lambda topic: topic['last_edited_by'],result)
        l = list(l)
        # Logger
        Logger.log_grean(message="\n ORDER BY GROUP:",value=l)
        Logger.log_grean(message="\n ORDERED BY GROUP:",value=sorted(l))
        self.assertTrue(sorted(l) == l)
        
    def testSortByLastModifiedDesc(self): 
        [result,expected] = self.getResultAndExpectedByKey("last_edited_by",False)
        l = map(lambda topic: topic['last_edited_by'],result)
        l = list(l)
        # Logger
        Logger.log_grean(message="\n ORDER BY GROUP:",value=l)
        Logger.log_grean(message="\n ORDERED BY GROUP:",value=sorted(l))
        self.assertTrue(sorted(l,reverse=True) == l)
        
    def testSortByAnswerNumAsc(self): 
        [result,expected] = self.getResultAndExpectedByKey("answer_num",True)
        l = map(lambda topic: topic['answer_num'],result)
        l = list(l)
        self.assertTrue(sorted(l) == l)
    
    def testSortByAnswerNumDesc(self): 
        [result,expected] = self.getResultAndExpectedByKey("answer_num",False)
        l = map(lambda topic: topic['answer_num'],result)
        l = list(l)
        self.assertTrue(sorted(l,reverse=True) == l)
        
    @classmethod 
    def tearDownClass(inst) -> None:
        inst.driver.quit()
    
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
        
        
        
# with webdriver.Firefox() as driver:
#     loginAndGetDiscussionList(driver)
#     star = driver.find_element(By.XPATH,first_star_path)
#     # Make sure no topic is starred 
#     while(star.get_attribute("title") != STAR_QUOTE):
#         # Unstar all the starred topic 
#         star.click()
#         WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, first_star_path))
#         star = driver.find_element(By.XPATH,first_star_path)
#     # Get discussion list  //*[@id="discussion-list-61821b5923ea261821b58bb28539"]/table/tbody/tr[1]
#     disc_list = driver.find_element(By.XPATH,disc_list_xpath)
#     discussion_list = disc_list.find_elements(By.XPATH,"*")
#     # print("List one len: ", len(disc_list_xpath),"List 2 len:",discussion_list,len(discussion_list))
#     for table_row in discussion_list: 
#         # topic_name = table_row.find_element(By.XPATH,"&")
#         star_link = table_row.find_element(By.XPATH,"td/a")
#         topic_name = table_row.find_element(By.XPATH,"th/div/a").get_attribute('title')
#         group_name = table_row.find_element(By.XPATH,"td[2]/a").get_attribute('innerHTML')
#         created_by = table_row.find_element(By.XPATH,"td[3]/div/div[2]/div[2]/time").get_attribute('innerHTML')
#         last_edited_by = table_row.find_element(By.XPATH,"td[4]/div/div[2]/div[2]/a/time").get_attribute('innerHTML')
#         answer_num = table_row.find_element(By.XPATH,"td[5]/span").get_attribute("innerText")
#         print(topic_name.strip(),group_name.strip(),created_by.strip(),last_edited_by.strip(),answer_num.strip())
   
   
    # for discussion in discussion_list:
    #     star = discussion.find_element(By.XPATH,"//td/a[@data-type='favorite-toggle']")
    #     topic_name = discussion.find_element(By.XPATH,"//th/div/a")
    #     # group = discussion.find_element(By.XPATH,"//td[@class='group align-middle']/a")
    #     # started_by = discussion.find_element(By.XPATH,"//td[@class='author']/div[@class='author-info align-middle']/div/")
    #     # last_update_by = discussion.find_element(By.XPATH,"//td/div[@class='author-info align-middle")
    #     print("Display star title", star.get_attribute('title'))
    #     print("Display topic title", topic_name.get_attribute('title'))
        # print("Display started user", started_by.get_attribute('innerText'))
        # print("started_by: ", started_by)
        # print("last_update_by: ", last_update_by)
        # /html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[4]/div/div[2]/div[2]/a/time
        # /html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th
    # topic = driver.find_element(By.XPATH,first_topic_path).click()
    # topic.click()
    # print(f"Topic value is: ", topic.get_attribute("title"))
    # driver.save_screenshot('./forum_testing_image.png')
    # /html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[3]/div/div[2]/div[1]
    # /html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[3]/div/div[2]/div[2]/time
    # /html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[3]/div/div[2]/div[2]/time
    # /html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[5]/span
    # first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    # print(first_result.get_attribute("textContent"))
    # assert(first_result.get_attribute("textContent") == "Cheese - asdfsdafWikipedia")
    
    
    # 
    # ! Use of counter to unstar a predefined number of topics 
    # max_count = 0
    # while(star.get_attribute("title") != STAR_QUOTE):
    #     # Unstar all the starred topic 
    #     star.click()
    #     WebDriverWait(driver,timeout=5).until(lambda d: d.find_element(By.XPATH, first_star_path))
    #     star = driver.find_element(By.XPATH,first_star_path)
    #     print("Star at iteration", max_count," is",star.get_attribute("title"))
    #     max_count = max_count + 1
    #     if max_count == 5: 
    #         break