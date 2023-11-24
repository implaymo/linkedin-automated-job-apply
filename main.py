from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

load_dotenv()

email_address = os.getenv("email")
pw = os.getenv("pw")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

# Open website
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3766025974&f_AL=true&f_E="
           "2&keywords=remote%20job%20search&origin=JOB_SEARCH_PAGE_JOB_FILTER")

sign_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
sign_in.click()

provide_email = driver.find_element(By.XPATH, '//*[@id="username"]')
provide_email.send_keys(f"{email_address}")

provide_pw = driver.find_element(By.XPATH, '//*[@id="password"]')
provide_pw.send_keys(f"{pw}")

sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()



## NOT WORKING, NEEDS FIXING
try:
    minimize_chat_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="ember42"]/svg/use'))
    )
    minimize_chat_button.click()

    print("Actions performed successfully!")
except TimeoutError:
    print("Timed out waiting for the element to be visible.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()



    # easy_apply = WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((By.XPATH, '//*[@id="ember228"]/span'))
    # )
    # easy_apply.click()
