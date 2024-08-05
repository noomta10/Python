from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_license():
    # Initialize the WebDriver 
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_service = webdriver.ChromeService(executable_path=r"C:\Users\itush\Documents\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service = chrome_service, options=options)

    # Navigate to the URL
    driver.get('https://marketplace.atlassian.com/apps/1226187/time-in-status-reports?hosting=datacenter&tab=overview')

    # Wait for the "Try it free" button to be clickable and click it
    try_it_free_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="app-listing__install-app-btn"]'))
    )
    try_it_free_button.click()

    # Fill in the email
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    email_input.send_keys('iglooteam1@gmail.com')

    # Click on the "Continue" button
    continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Continue"]')))
    continue_button.click()

    # Click on "Continue with Google" button
    continue_with_google_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Continue with Google"]')))
    continue_with_google_button.click()

    # Switch to Google login window
    driver.switch_to.window(driver.window_handles[-1])

    # Fill in the Google email
    google_email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId')))
    google_email_input.send_keys('iglooteam1@gmail.com')
    google_email_input.send_keys(Keys.ENTER)

    # Wait for the password input
    google_password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Passwd')))
    google_password_input.send_keys('devspace123')
    google_password_input.send_keys(Keys.ENTER)

    driver.switch_to.window(driver.window_handles[0])

    # Wait for the organization name input to be visible and fill it
    org_input = WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.ID, 'organisation_name')))
    org_input.send_keys('MOD')

    # Check the first checkbox
    checkbox1 = driver.find_element(By.ID, 'marketplaceTermsConfirm')
    checkbox1.click()

    # Check the second checkbox
    checkbox2 = driver.find_element(By.ID, 'vendorTermsConfirm')
    checkbox2.click()

    # Click on the "Generate License" button
    generate_license_button = driver.find_element(By.XPATH, '//span[contains(text(), "Generate License")]/..')
    generate_license_button.click()

    # Wait for the license key to be visible and print it
    license_key = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'license-key'))
    )
    print(license_key.get_attribute('value'))

    # Close the WebDriver
    driver.quit()

def main():
    get_license()

if __name__ == "__main__":
    main()