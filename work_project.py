import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

url = # URL for work address
driver = webdriver.Firefox()
driver.set_window_size(1000, 700)
driver.get(url)
part_list = []

# Login info Hard coded instead of using files
# Personally don't recommend this as it's not secure being hard coded in your script. 
class WORD_INPUT:

    id_service = ""
    id_name = ""
    id_pass = ""
    email = ""
    email_pass = ""


def back_page():
    driver.get(# Website for work)


def word_entry(el, word):
    word = str(word)
    for i in word:
        el.send_keys(i)


def waiting_for_el(el):
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, el)))

# Enter UserID
waiting_for_el("/html/body/div[1]/div/form[1]/div[2]/div/div[1]/input")
servicebench = driver.find_element_by_xpath("/html/body/div[1]/div/form[1]/div[2]/div/div[1]/input")
word_entry(servicebench, WORD_INPUT.id_service)
# Enter NameID
waiting_for_el("/html/body/div[1]/div/form[1]/div[2]/div/div[2]/input")
userid = driver.find_element_by_xpath("/html/body/div[1]/div/form[1]/div[2]/div/div[2]/input")
word_entry(userid, WORD_INPUT.id_name)
# Enter PssID
waiting_for_el("/html/body/div[1]/div/form[1]/div[2]/div/div[3]/input[1]")
psswrd = driver.find_element_by_xpath("/html/body/div[1]/div/form[1]/div[2]/div/div[3]/input[1]")
word_entry(psswrd, WORD_INPUT.id_pass)
# Login
waiting_for_el("/html/body/div[1]/div/form[1]/div[2]/div/div[4]/input")
enter_key = driver.find_element_by_xpath("/html/body/div[1]/div/form[1]/div[2]/div/div[4]/input").click()
#
waiting_for_el("/html/body/div[2]/div[1]/div[1]/section/table/tbody/tr[2]/td/a")
direct = driver.find_element_by_css_selector("#jobs > table:nth-child(3) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1)")
direct_num = int(direct.text)
direct.click()

if direct_num == 0:
    print("No Jobs To List")
else:
    print("You have {} Jobs".format(direct_num))


for i in range(2, direct_num * 2 + 2, 2):
    small_list = []
    waiting_for_el("/html/body/div[2]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[1]/a")
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/table/tbody/tr[" + str(i) + "]/td[1]/a").click()

    try:
        # WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/form[1]/fieldset[5]/table/tbody/tr/td/fieldset/table/tbody/tr/td[3]")))
        tech = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form[1]/fieldset[5]/table/tbody/tr/td/fieldset/table/tbody/tr/td[3]")
        small_list.append(tech.text)
    except:
        small_list.append("Tech Not Assigned")
        pass


    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/form[1]/fieldset[7]"
                                                                              "/table/tbody/tr[1]/td/fieldset/div/div[1]"
                                                                              "/div[2]/div[7]/div[2]")))
    part_number = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form[1]/fieldset[7]/table/tbody/tr[1]/td/fieldset/div/div[1]/div[2]/div[7]/div[2]")
    city = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form[1]/fieldset[1]/table/tbody/tr[5]/td[1]/div[4]")
    time_frame = driver.find_element_by_xpath("/html/body/div[2]/div[1]/form[1]/fieldset[3]/table/tbody/tr[1]/td[2]")

    small_list.extend((part_number.text, city.text, time_frame.text))
    part_list.append(small_list)
    back_page()

for i in part_list:
    print(i)
driver.close()

driver = webdriver.Firefox()
driver.set_window_size(1000,700)
driver.get(# Goes to Email)
waiting_for_el("//*[@id='i0116']")
email_el = driver.find_element_by_xpath("//*[@id='i0116']")
word_entry(email_el, WORD_INPUT.email)
driver.find_element_by_xpath("//*[@id='idSIButton9']").click()

# password for email
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='i0118']")))
pass_el = driver.find_element_by_xpath("//*[@id='i0118']")
word_entry(pass_el, WORD_INPUT.email_pass)
driver.find_element_by_xpath("//*[@id='idSIButton9']").click()
time.sleep(0.8)
driver.find_element_by_xpath("//*[@id='iLandingViewAction']").click()
