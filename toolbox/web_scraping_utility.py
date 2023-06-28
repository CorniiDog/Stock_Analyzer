import os, time
from selenium import webdriver
# Add headless option
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

def test_headless(website, screenshot_path, screen_width=1920, screen_height=1080):

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Initialize the Chrome webdriver and pass the options
    driver = webdriver.Chrome(options=options)

    driver.set_window_size(screen_width, screen_height)

    driver.get(website)

    # If path doesn't have a .png extension, add it
    if not screenshot_path.endswith('.png'):
        screenshot_path += '.png'

    # Take screenshot
    driver.save_screenshot(screenshot_path)

    driver.quit()


if __name__ == '__main__':
    test_headless('https://www.google.com', 'test')
