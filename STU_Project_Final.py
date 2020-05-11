from selenium import webdriver
import time,pytesseract
from PIL import Image

Favorite_food_1 = input("(شويدپلو با گوشت / قيمه سيب زميني) : غذاي روز شنبه")
Favorite_food_2 = input("(استانبولي / شنيسل مرغ) : غذاي روز يکشنبه")
Favorite_food_3 = input("(کوفته / کنسرو تن ماهي) : غذاي روز دوشنبه")
Favorite_food_4 = input("(کوکو سبزي / کوبيده) : غذاي روز سه شنبه")

User = '********'     #Username and password
Pass = '********'

driver_path = r"C:\Users\CHS\Desktop\MicrosoftWebDriver.exe"
driver = webdriver.Edge(driver_path)                  #location of chrome webdriver

driver.get("http://stu.iust.ac.ir/loginpage.rose")  # the determined URL

elem = driver.find_element_by_id('j_username')
elem.send_keys(User)

time.sleep(1)                                   #applying Username and password

elem = driver.find_element_by_id('j_password')
elem.send_keys(Pass)

IM_OBJ = driver.find_element_by_id('captcha_img')
Saved_IM = IM_OBJ.screenshot('captcha.png')
captcha = Image.open('captcha.png','r')
captcha_string = pytesseract.image_to_string(captcha, lang='eng')

elem = driver.find_element_by_id('captcha_input')
elem.click()
elem.send_keys(captcha_string)

time.sleep(3) #time required to fill the Captcha Input Field

driver.find_element_by_xpath('//*[@id="login_btn_submit"]').click()  #logging in

time.sleep(5)

driver.find_element_by_xpath('//*[@id="1_div"]/div[1]/a/img').click()

time.sleep(8)

A = driver.find_element_by_id('nextWeekBtn')
A.click()


time.sleep(8)



                              
if Favorite_food_1 == "قيمه سيب زميني":
    
    driver.find_element_by_xpath('//*[@id="userWeekReserves.selected1"]').click()

else:
    driver.find_element_by_xpath('//*[@id="userWeekReserves.selected0"]').click()


    

time.sleep(2)



                                                             #selecting food for a week

if Favorite_food_2 == "شنيسل مرغ":
    
    driver.find_element_by_xpath('//*[@id="userWeekReserves.selected3"]').click()

else:
    driver.find_element_by_xpath('//*[@id="userWeekReserves.selected2"]').click()
    

    

time.sleep(2)




if Favorite_food_3 == "کنسرو تن ماهي":
    
    driver.find_element_by_xpath('//*[@id="userWeekReserves.selected5"]').click()

else:
    driver.find_element_by_xpath('//*[@id="userWeekReserves.selected4"]').click()


    

time.sleep(2)



if Favorite_food_4 == "کوکو سبزي":
    
    driver.find_element_by_xpath('//*[@id="userWeekReserves.selected6"]').click()

else:
    driver.find_element_by_xpath('//*[@id="userWeekReserves.selected7"]').click()


    

time.sleep(3)


driver.find_element_by_xpath('//*[@id="doReservBtn"]').click()       #Reservation


time.sleep(5)


driver.quit()        #DONE:D


