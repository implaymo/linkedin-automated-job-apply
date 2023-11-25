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
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3754274123&f_AL="
           "true&f_E=2&keywords=remote%20job%20search&origin=JOB_SEARCH_PAGE_JOB_FILTER")

driver.maximize_window()

sign_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
sign_in.click()

provide_email = driver.find_element(By.XPATH, '//*[@id="username"]')
provide_email.send_keys(f"{email_address}")

provide_pw = driver.find_element(By.XPATH, '//*[@id="password"]')
provide_pw.send_keys(f"{pw}")

sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()


time.sleep(5)

def save_job():
    """Clicks SAVE to save the job"""
    try:
        save_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]'
                                                        '/div/div[2]/div/div[1]/div/div[1]/div'
                                                        '/div[1]/div[1]/div[4]/div/button'))
        )
        save_button.click()
    except TimeoutError:
        print("Timed out waiting for the element to be visible.")
    except Exception as e:
        print(f"An error occurred saving jobs: {e}")

def scroll_down():
    try:
        # Find the scrollable element
        scroll_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'jobs-search-results-list')))

        # Scroll a fixed amount (you can adjust the value based on your preference)
        driver.execute_script("arguments[0].scrollBy(0, 50);", scroll_element)
    except Exception as e:
        print(f"An error occurred scrolling: {e}")

def check_if_saved():
    saved = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]'
                                          '/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button/span[1]')
    return saved.text


# Find all jobs
jobs = WebDriverWait(driver, 10).until(
    EC.visibility_of_any_elements_located((By.CLASS_NAME, 'disabled.ember-view.'
                                                          'job-card-container__link.job-card-list__title')))
while True:
    try:
        for i in range(len(jobs)):
            # Re-locate the jobs after each iteration
            jobs = WebDriverWait(driver, 10).until(
                EC.visibility_of_any_elements_located((By.CLASS_NAME, 'disabled.ember-view.'
                                                                      'job-card-container__link.job-card-list__title'))
            )
            # Click the new job on the list
            jobs[i].click()

            # Checks if Bot as already saved job
            if check_if_saved() == "Saved":
                scroll_down()
                time.sleep(2)
                continue


            # Introduce a delay
            time.sleep(2)
            save_job()
            scroll_down()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

