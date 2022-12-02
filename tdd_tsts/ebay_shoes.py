from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.ebay.com/')

# Locators
SRCH_FLD = (By.XPATH, "//input[@class='gh-tb ui-autocomplete-input']")
SRCH_BTN = (By.XPATH, "//input[@class = 'btn btn-prim gh-spr']")
XPCTD_MSG = (By.XPATH, "(//*[contains(text(),'Clothing, Shoes & Accessories')])[2]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# In search field type "Shoes"
wait.until(EC.presence_of_element_located(SRCH_FLD)).clear()
wait.until(EC.presence_of_element_located(SRCH_FLD)).send_keys('Shoes')
sleep(4)

# Click on the Search button
wait.until(EC.element_to_be_clickable(SRCH_BTN)).click()

# Verify that the text "Clothing, Shoes & Accessories" is here
expected = ('Clothing, Shoes & Accessories!')
actual = (wait.until(EC.presence_of_element_located(XPCTD_MSG)).text)
# assert expected in actual,  f'Error. Expected text: {expected}, but actual text is: {actual}'
if expected in actual:
    print(f'Actual is OK:\n"{actual}"\n')
else:
    print(f'Error, expected: "{expected}", but got "{actual}"\n')

# Find iframes
iframes = driver.find_elements(By.TAG_NAME, 'iframe')
print(f'Number of iframes: {len(iframes)}; type of iframes: {type(iframes)}')
print(f'iFrames: {iframes}')

# Sleep to see what we have
sleep(4)

# Driver quit
driver.quit()