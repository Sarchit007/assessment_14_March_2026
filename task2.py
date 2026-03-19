# Question2
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.youtube.com")
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[name="search_query"]').send_keys("melody hits")
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"').click()
