# question3
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.find_element(By.ID,"register_Layer").click()
driver.find_element(By.ID,"name").send_keys("Archit")
driver.find_element(By.ID,"email").send_keys("sarchit971@gmail.com")
driver.find_element(By.ID,"password").send_keys("pass")

