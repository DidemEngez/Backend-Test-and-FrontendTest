from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()  

driver.get("https://flights-app.pages.dev/")

try:
    wait = WebDriverWait(driver, 100)

    from_input = wait.until(EC.element_to_be_clickable((By.ID, 'from')))
    to_input = wait.until(EC.element_to_be_clickable((By.ID, 'to')))

    from_input.send_keys("IST")
    to_input.send_keys("IST")
    
    time.sleep(2)
    
    assert from_input.get_attribute('value') != to_input.get_attribute('value'), "Bug: 'From' ve 'To' değerleri aynı olabiliyor."

    flights_list = driver.find_elements(By.CLASS_NAME, 'flight-item')
    found_items_text = driver.find_element(By.CLASS_NAME, 'found-items').text
    found_count = int(found_items_text.split(' ')[1])
    
    assert found_count == len(flights_list), f"Listelenen uçuş sayısı ile 'Found {found_count} items' yazısı uyuşmuyor."

finally:
    driver.quit()







