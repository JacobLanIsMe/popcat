from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("/Users/kaohuiling1108/Documents/popcat/chromedriver")
driver.get("https://popcat.click/?fbclid=IwAR3CW5KILkvfCSsAysw7jILWKYZNgeV4Fp28555fHEcvGMef_owLexBAbNM")
#time.sleep(5)
driver.implicitly_wait(10)
ele = driver.find_element_by_css_selector(".cat-img")
for i in range(8889999999999999999999999999999999999999999999999):
    if i < 8889999999999999999999999999999999999999999999999:
        ele.click()

