from selenium import webdriver
import time

User = '96521236'     #Username and password
Pass = '4830137614'

driverpath = r"C:\Users\CHS\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driverpath)                  #location of chrome webdriver

driver.get("http://stu.iust.ac.ir/loginpage.rose")  # the determined URL

elem = driver.find_element_by_id('j_username')
elem.send_keys(User)

time.sleep(1)                                   #applying Username and password
 

elem = driver.find_element_by_id('j_password')
elem.send_keys(Pass)

time.sleep(8) #time required to fill the Captcha Input Field

driver.find_element_by_xpath('//*[@id="login_btn_submit"]').click()  #logging in

time.sleep(2)

driver.find_element_by_xpath('//*[@id="1_div"]/div[1]/a/img').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="nextWeekBtn"]').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="nextWeekBtn"]').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="userWeekReserves.selected1"]').click()

time.sleep(2)                                                                     #selecting food for two days

driver.find_element_by_xpath('//*[@id="userWeekReserves.selected3"]').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="doReservBtn"]').click()       #Reservation

time.sleep(5)


driver.quit()        #DONE:D


