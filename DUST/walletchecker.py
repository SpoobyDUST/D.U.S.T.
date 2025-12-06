from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time

# URL of the Solscan page
url = "https://solscan.io/account/7q5Qa5TCoNLfSiVk2MPU8pA1e9L2THqpZSQ7ARZrSpUa#portfolio"
# Token address to search for
token_address_to_search = "4eg9qFUEZnBvwioRkrdtaEdaqJVtv2zzY68yPgU8pKba"

# Initialize the WebDriver using WebDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Load the webpage
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Find the "Portfolio" button
portfolio_button = driver.find_element(By.XPATH, '//button[contains(text(), "Portfolio")]')

# Click the "Portfolio" button to activate the portfolio section
portfolio_button.click()

# Wait for the portfolio section to load (you may need to adjust the timeout)
driver.implicitly_wait(10)

# Find the token search input field
token_search_input = driver.find_element(By.ID, "token-search")

# Enter the token address into the input field
token_search_input.send_keys(token_address_to_search)

# Simulate pressing Enter to perform the search (optional)
token_search_input.send_keys(Keys.RETURN)

# Wait for the token address to appear (you may need to adjust the timeout)
time.sleep(5)  # Adjust the time as needed

# Get the position of the token address on the screen
token_address_position = pyautogui.locateOnScreen('token_address.png', confidence=0.8)

# If the token address is found on the screen, click on it
if token_address_position:
    pyautogui.click(token_address_position)
else:
    print("Token address not found on the screen.")

# Close the WebDriver
driver.quit()
