from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import unittest
import random
from ddt import ddt, data, file_data, idata, unpack



from Util import getCurrentDisccusionList, login_to_topic_page, loginAndGetDiscussionList

# Shuold star the topic with name TEST_SORT first 
test_topic_xpath = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/th/div/a'

answer_button_xpath = 'a.btn:nth-child(2)'
answer_box_xpath = '/html/body/div[2]/div[3]/div/div/section/div[1]/form/fieldset/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div'

comment_submit_button_xpath = '/html/body/div[2]/div[3]/div/div/section/div[1]/form/div[2]/div[2]/fieldset/div/div[1]/span/input'
message = "AUTO_COMMENT"
                    #"""/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[2]/div[3]/a[1]"""
new_comment_xpath = "/html/body/div[2]/div[3]/div/div/section/div[1]/div/article/div[2]/div[2]/a[1]"
comment_list_container_xpath = '/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[2]'

new_comment_edit_xpath = "/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div/div[2]/div[2]/div/a[3]"
new_comment_title_xpath = "/html/body/div[2]/div[3]/div/div/section/div[1]/form/fieldset/div/div[1]/div[2]/input"

new_comment_edit_box_xpath = '/html/body/div[2]/div[3]/div/div/section/div[1]/form/fieldset/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div'
new_comment_edit_submit_button_xpath = '/html/body/div[2]/div[3]/div/div/section/div[1]/form/div[2]/div[2]/fieldset/div/div[1]/span/input'

add_file_button_xpath = '/html/body/div[3]/div[3]/div/div/section/div[1]/form/fieldset/div/div[4]/div[2]/fieldset/div/div[4]/div[1]/div[2]'
add_file_button_css_selector = '#yui_3_17_2_1_1636011194271_535 > div.fm-content-wrapper > div.fm-empty-container > div > div'
personal_storage_button_xpath ='/html/body/div[9]/div[3]/div/div[2]/div/div/div[1]/div[3]/a/span'
file_xpath = '/html/body/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/tbody/tr/td[3]/span/a/span[2]'
confirm_file_button_xpath = '/html/body/div[10]/div[3]/div/div[2]/div/div[2]/form/div[4]/div/button[1]'
save_changes_button_xpath = '/html/body/div[3]/div[3]/div/div/section/div[1]/form/div[2]/div[2]/fieldset/div/div[1]/span/input'

@ddt
class EditCommentTest(unittest.TestCase):
    @classmethod 
    def setUpClass(inst): 
        inst.debug = True
        # Create a new Firefox session 
        inst.driver = webdriver.Firefox() 
        wait = WebDriverWait(inst.driver, 10) 
        inst.maxDiff = None
        # Go to the topic page 
        login_to_topic_page(inst.driver)    
        # Find the test topic and comment on it 
        inst.driver.find_element(By.XPATH,test_topic_xpath).click() 
        WebDriverWait(inst.driver,timeout=30).until(lambda d: d.find_element(By.CSS_SELECTOR, answer_button_xpath))
        answer_button =  inst.driver.find_element(By.CSS_SELECTOR,answer_button_xpath)         
        answer_button.click() 
        WebDriverWait(inst.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, answer_box_xpath))

        answer_box = inst.driver.find_element(By.XPATH,answer_box_xpath) 
        answer_box.click() 
        random_message_post_fix = random.random() * 10000000
        inst.message = f"{message}{random_message_post_fix}"
        answer_box.send_keys(inst.message)
        if inst.debug: 
            print(f"Thinh commented message with content: {inst.message}")

        inst.driver.find_element(By.XPATH,comment_submit_button_xpath).click()  
        # Go back and find the newly created comment 
        WebDriverWait(inst.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, comment_list_container_xpath))
        replies_container = inst.driver.find_element(By.XPATH,comment_list_container_xpath)
        comments_num = len(replies_container.find_elements(By.XPATH,'*'))
        
        if inst.debug: 
            print(f"Currently there are {comments_num} comments")
        inst.comments_num = comments_num
        if inst.debug: 
            print(f"New comment xpath is: {new_comment_xpath}")
        WebDriverWait(inst.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, comment_list_container_xpath))
        replies_container = inst.driver.find_element(By.XPATH,comment_list_container_xpath)
        # Click the newly created comment 
        replies_container.find_element(By.XPATH,f'div[{inst.comments_num}]/a[1]').click() 
        WebDriverWait(inst.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, new_comment_edit_xpath))
        inst.driver.find_element(By.XPATH,new_comment_edit_xpath).click()
        inst.driver.save_screenshot(f'image.png')
        # /html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[2]/div[9]/a[1]
        # Make edit and test on it (In the testcases)
    
    
    # Precondition. We MUST be in the page that contains the list before calling this function 
    def get_nth_message_in_message_list(self,message_num=0):  
        WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, comment_list_container_xpath))
        replies_container = self.driver.find_element(By.XPATH,comment_list_container_xpath)
        # Return the ith message in the list  
        return replies_container.find_element(By.XPATH,f'div[{message_num}]/a[1]')
    
    def findNewlyEditedComment(self):
        return self.get_nth_message_in_message_list(self.comments_num)  
    
    def submit_edit(self):
        # Refind the edited message 
        WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, new_comment_edit_submit_button_xpath))
        self.driver.find_element(By.XPATH,new_comment_edit_submit_button_xpath).click() 
    
    # ? Precondition: The file choosing box must be presnet 
    def choose_file_with_filename(self,filename=""):
        file_link_text = self.driver.find_elements_by_xpath(f"//*[contains(text(), '{filename}')]")
        return file_link_text
    
    def testChangeCommentRandomText(self): 
        new_message = "RANDOM_TEST_DATA"
        WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, new_comment_title_xpath))
        edit_box = self.driver.find_element(By.XPATH,new_comment_edit_box_xpath)
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
        self.assertEqual(new_comment_content.strip(),new_message)
        self.driver.back()
        self.driver.save_screenshot('./image.png')
        
        
    @data(('Thinh is a god', 'Thinh is a god'), ('God is thinh', 'God is thinh'), ('God does exist', 'God does exist'))
    @unpack
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
            
    # def testMediaAttachment(self): 
    #     file_name_to_click = 'alice.txt'
    #     self.driver.save_screenshot('./image.png')

    #     # Click the add file item
    #     WebDriverWait(self.driver,timeout=10).until(lambda d: d.find_element(By.CSS_SELECTOR, add_file_button_css_selector))
    #     # wait1 = WebDriverWait(self.driver, 10);
    #     # element1 = wait1.until(EC.element_to_be_clickable(By.XPATH(add_file_button_xpath)));
    #     self.driver.find_element(By.XPATH,add_file_button_css_selector).click()

    #     # self.driver.find_element(By.XPATH,add_file_button_xpath).click()        
    #     # Choose Personal Storage 
    #     WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH, personal_storage_button_xpath))
    #     self.driver.find_element(By.XPATH,personal_storage_button_xpath).click() 
    #     # Choose the file with file name   
    #     file = self.choose_file_with_filename(file_name_to_click) 
    #     file.click() 
    #     # Click confirm 
    #     WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH,confirm_file_button_xpath))
    #     self.driver.find_element(By.XPATH,confirm_file_button_xpath).click()
    #     # Submit edit 
    #     WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH,save_changes_button_xpath))
    #     self.driver.find_element(By.XPATH,save_changes_button_xpath).click()
    #     # Go back to the editted comment 
    #     new_comment = self.findNewlyEditedComment() 
    #     new_comment.click() 
    #     new_comment_content_xpath = '/html/body/div[1]/div[3]/div/div/section/div[1]/div/article/div[1]/div/div/div[2]/div[1]'

    #     WebDriverWait(self.driver,timeout=30).until(lambda d: d.find_element(By.XPATH,new_comment_content_xpath))
    #     self.driver.save_screenshot(f'image.png')
    #     # Find the file name: 
    #     file = self.choose_file_with_filename(file_name_to_click) 
    #     file_added_name = file.get_attribute('innerText')
    #     self.assertEqual(file_added_name == file_name_to_click)        
        # Check if the message is edited 
        # new_comment_content = self.driver.find_element(By.XPATH,new_comment_content_xpath).get_attribute('innerText')
        # print(f"Entered Message is: {new_message}\nFound Message is: {new_comment_content}")
        # self.assertEqual(new_comment_content.strip(),new_message)
    
    # def testMediaAttachByLink(self):
    #     pass 

    @classmethod 
    def tearDownClass(inst) -> None:
        inst.driver.quit()
        
        

        
if __name__ == '__main__':
    unittest.main(verbosity=2)
        
        
        
        