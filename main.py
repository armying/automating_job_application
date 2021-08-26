from selenium import webdriver
import time

CHROME_DRIVER_LOCATION = "C:/Users/Army/Desktop/Development/chromedriver.exe" # Your chromedriver location
WEBSITE = "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WRA=true&geoId=103644278&keywords=entry%20software%20engineer&location=United%20States"
email = "ENTER YOUR EMAIL"
my_pass = "ENTER YOUR PASSWORD"


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_LOCATION)
driver.get(WEBSITE)

sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()

first_step = False
second_step = False

time.sleep(3)

email_entry = driver.find_element_by_xpath('//*[@id="username"]')
email_entry.send_keys(email)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(my_pass)

button = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
button.click()

time.sleep(5)
job = driver.find_element_by_css_selector(".jobs-s-apply")
job.click()

time.sleep(5)
phone_number = driver.find_element_by_class_name(".fb-single-line-text__input")
if phone_number.text == "":
    phone_number.send_keys("9255489429")

time.sleep(5)
next_button = driver.find_elements_by_css_selector("footer button")
next_button.click()


