from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

# question1
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.facebook.com")
driver.find_element(By.CSS_SELECTOR, "input#R_1h6kqsqppb6amH1").send_keys("Archit")
driver.find_element(By.CSS_SELECTOR, "input#R_1hmkqsqppb6amH1").send_keys("pass")
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"').click()

# question2
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.youtube.com")
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[name="search_query"]').send_keys("melody hits")
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"').click()


# question3
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.find_element(By.ID,"register_Layer").click()
driver.find_element(By.ID,"name").send_keys("Archit")
driver.find_element(By.ID,"email").send_keys("sarchit971@gmail.com")
driver.find_element(By.ID,"password").send_keys("pass")

# question4
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://www.myntra.com")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"desktop-searchBar").send_keys("tshirt")