from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_instagram_followers_and_following():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Use the appropriate driver for your browser
    driver.get("https://www.instagram.com/guviofficial/")

    try:
        # Wait until the followers and following elements are present
        followers_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers/')]/span"))
        )
        following_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/following/')]/span"))
        )

        # Extract the number of followers and following
        followers = followers_element.get_attribute('title')  # The title attribute contains the followers count
        following = following_element.text  # The text of the span element contains the following count

        print(f"Total Followers: {followers}")
        print(f"Total Following: {following}")

    finally:
        # Close the WebDriver
        driver.quit()

if _name_ == "_main_":
    get_instagram_followers_and_following()