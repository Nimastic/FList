from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your geckodriver executable
webdriver_path = '/path/to/geckodriver'  # Update this to the actual path

# Configure the WebDriver (using Firefox in this example)
service = Service(webdriver_path)
options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")
driver = webdriver.Firefox(service=service, options=options)

def login_to_instagram(username, password):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)  # Wait for the login page to load

    # Find username and password fields and enter login credentials
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    
    time.sleep(5)  # Wait for login to complete

def get_followers(username):
    driver.get(f'https://www.instagram.com/{username}/followers/')
    time.sleep(5)  # Wait for the page to load
    
    followers = set()
    scroll_box = driver.find_element(By.XPATH, "//div[@role='dialog']//div[@class='_aano']")
    last_height = driver.execute_script("return arguments[0].scrollHeight", scroll_box)
    
    while True:
        elements = scroll_box.find_elements(By.CSS_SELECTOR, 'a.FPmhX.notranslate._0imsa')
        for element in elements:
            followers.add(element.text)
        
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scroll_box)
        time.sleep(2)
        
        new_height = driver.execute_script("return arguments[0].scrollHeight", scroll_box)
        if new_height == last_height:
            break
        last_height = new_height
    
    return list(followers)

def get_following(username):
    driver.get(f'https://www.instagram.com/{username}/following/')
    time.sleep(5)  # Wait for the page to load
    
    following = set()
    scroll_box = driver.find_element(By.XPATH, "//div[@role='dialog']//div[@class='_aano']")
    last_height = driver.execute_script("return arguments[0].scrollHeight", scroll_box)
    
    while True:
        elements = scroll_box.find_elements(By.CSS_SELECTOR, 'a.FPmhX.notranslate._0imsa')
        for element in elements:
            following.add(element.text)
        
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scroll_box)
        time.sleep(2)
        
        new_height = driver.execute_script("return arguments[0].scrollHeight", scroll_box)
        if new_height == last_height:
            break
        last_height = new_height
    
    return list(following)

username = 'jerielczy'  # Replace with your Instagram username
password = 'your_password'  # Replace with your Instagram password

login_to_instagram(username, password)

followers = get_followers(username)
print("Followers:", followers)

following = get_following(username)
print("Following:", following)

driver.quit()
