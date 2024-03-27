from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

CHROME_DRIVER_PATH = 'C:/Users/ual-laptop/Desktop/Icons/Data Mining/Test_Scraping/chromedriver.exe'
LINKEDIN_URL = 'https://www.linkedin.com/'

USERNAME= '#@#%@%@%'
PASSWORD= '##@#%@%@%'

def login(driver):
    driver.get(LINKEDIN_URL)
    time.sleep(2)  # Wait for page to load

    # Log in to LinkedIn
    username_input = driver.find_element(By.XPATH, '//input[@name="session_key"]')
    password_input = driver.find_element(By.XPATH, '//input[@name="session_password"]')
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)  # Wait for login

def search_recruiters(driver, country):
    # Navigate to the LinkedIn search page
    # Navigate to the LinkedIn search page with search as "Recruiter" from "United States"
    driver.get('https://www.linkedin.com/search/results/people/?keywords=Recruiter&origin=SWITCH_SEARCH_VERTICAL&geoUrn=%5B%22103644278%22%5D')

    time.sleep(10)  # Wait for page to load

    # Filter search results by country
    # Click on 'All filters' button
    # all_filters_button = driver.find_element(By.XPATH, '//button[@aria-label="All filters"]')
    # all_filters_button.click()
    # time.sleep(2)  # Wait for modal to load

def extract_recruiter_profiles(driver):
    # Extract recruiter profile URLs from search results
    recruiter_urls = []
    page_count = 0
    while page_count < 3:
        # Extract recruiter profile URLs
        recruiter_links = driver.find_elements(By.XPATH, '//a[contains(@class, "app-aware-link")]')
        recruiter_urls = [link.get_attribute('href') for link in recruiter_links]

        # Check if there is a 'Next' button
        next_button = driver.find_elements(By.XPATH, '//button[@aria-label="Next"]')
        if next_button and next_button[0].get_attribute('disabled'):
            break
        elif next_button:
            next_button[0].click()
            page_count += 1
    
    return recruiter_urls

def send_connection_requests(driver, recruiter_urls):
    # Send connection requests to recruiters
    for recruiter_url in recruiter_urls:
        driver.get(recruiter_url)
        time.sleep(2)  # Wait for page to load

        # Check if 'Connect' button is available
        connect_button = driver.find_element_by_xpath('//button[@aria-label="Connect"]')
        if connect_button:
            connect_button.click()
            time.sleep(2)  # Wait for modal to load

            # Send the connection request
            send_button = driver.find_element_by_xpath('//button[@aria-label="Send now"]')
            send_button.click()
            print(f"Connection request sent to {recruiter_url}")

def main():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    
    try:
        # Log in to LinkedIn
        login(driver)

        # Search recruiters based on country
        search_recruiters(driver, 'United States')

        # Extract recruiter profile URLs from search results
        recruiter_urls = extract_recruiter_profiles(driver)
        with open('recruiter_urls.txt', 'w') as f:
            for url in recruiter_urls:
                if "miniProfile" in url:
                    f.write(f"{url}\n")
        # Send connection requests to recruiters
        #send_connection_requests(driver, recruiter_urls)

    finally:
        # Close the browser
        driver.quit()

if __name__ == '__main__':
    main()