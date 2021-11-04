from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC

login_button_xpath = "//*[@id='region-main']/div/div[2]/div/div/div/div[2]/div/div/div[1]/a"
software_testing_course_link_xpath = "/html/body/div[2]/div[3]/div/div/section[1]/div/aside/section/div/div/div[1]/div/div/div/div[1]/div/ul/ul[1]/li[9]/div/div/div/a"
test_forum_xpath = "/html/body/div[1]/div[3]/div/div/section/div/div/ul/li[3]/div[3]/ul/li[11]/div/div/div[2]/div/a"

first_star_path = "/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[1]/a"
first_topic_path = "//*[@id='yui_3_17_2_1_1635876930203_521']"
# '''/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[1]/a/span/i '''
STAR_QUOTE = 'Star this discussion'
UNSTAR_QUOTE = 'Unstar this discussion'
#yui_3_17_2_1_1635916493586_512
#yui_3_17_2_1_1635916493586_513
# Discussion List 
disc_list_xpath = '/html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody'

def login_to_topic_page(driver):
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
    WebDriverWait(driver,timeout=30).until(lambda d: d.find_element(By.XPATH, software_testing_course_link_xpath))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,  software_testing_course_link_xpath))).click()
    # Navigate to the test forum 
    WebDriverWait(driver,timeout=30).until(lambda d: d.find_element(By.XPATH, test_forum_xpath))
    driver.find_element(By.XPATH, test_forum_xpath).click()
    # Find the first star element 
    WebDriverWait(driver,timeout=30).until(lambda d: d.find_element(By.XPATH, first_star_path))    


def loginAndGetDiscussionList(driver): 
    login_to_topic_page(driver)    
    return getCurrentDisccusionList(driver)

def getCurrentDisccusionList(driver):
    return_list = [] 
    # Get discussion list  //*[@id="discussion-list-61821b5923ea261821b58bb28539"]/table/tbody/tr[1]
    disc_list = driver.find_element(By.XPATH,disc_list_xpath)
    discussion_list = disc_list.find_elements(By.XPATH,"*")
    # print("List one len: ", len(disc_list_xpath),"List 2 len:",discussion_list,len(discussion_list))
    for table_row in discussion_list: 
        # topic_name = table_row.find_element(By.XPATH,"&")
        # star_link = table_row.find_element(By.XPATH,"td/a")
        topic_name = table_row.find_element(By.XPATH,"th/div/a").get_attribute('title')
        group_name = table_row.find_element(By.XPATH,"td[2]/a").get_attribute('innerHTML')
        created_by = table_row.find_element(By.XPATH,"td[3]/div/div[2]/div").get_attribute('innerText')
        last_edited_by = table_row.find_element(By.XPATH,"td[4]/div/div[2]/div[2]/a/time").get_attribute('data-timestamp')
        # /html/body/div[2]/div[3]/div/div/section/div[2]/div/table/tbody/tr[1]/td[4]/div/div[2]/div[2]/a/time
        answer_num = table_row.find_element(By.XPATH,"td[5]/span").get_attribute("innerText")
        return_list.append({
            'topic_name': topic_name.strip().lower(), 
            'group_name': group_name.strip(), 
            'created_by': created_by.strip(),
            'last_edited_by': int(last_edited_by.strip()),
            'answer_num': int(answer_num.strip().lower())
        })
    return return_list
    
    # first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
    # print(first_result.get_attribute("textContent"))
    # assert(first_result.get_attribute("textContent") == "Cheese - asdfsdafWikipedia")
  
  
  