import os, time
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--headless=new')


def test_headless(website: str, screenshot_path, screen_width: int = 1920, screen_height: int = 1080):
    """
    Parameters
    ----------
    website: str
        The website to take a screenshot of
    screenshot_path: str
        The path to save the screenshot to
    screen_width: int
        The width of the screen to take the screenshot of
    screen_height: int
        The height of the screen to take the screenshot of

    Returns
    -------
    None

    Note
    ----
    The screenshot will be saved as a .png file
    This function is built just to test the headless option of selenium.

    Example
    -------
    from toolbox import web_scraping_utility
    import os
    current_dir = os.getcwd()

    screenshot_path = os.path.join(current_dir, 'test')
    web_scraping_utility.test_headless('https://www.youtube.com', screenshot_path)
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    # Initialize the Chrome webdriver and pass the options
    driver = webdriver.Chrome(options=options)

    driver.set_window_size(screen_width, screen_height)

    driver.get(website)

    # If path doesn't have a .png extension, add it
    if not screenshot_path.endswith('.png'):
        screenshot_path += '.png'

    time.sleep(4)

    # Take screenshot
    driver.save_screenshot(screenshot_path)

    driver.quit()


if __name__ == '__main__':
    test_headless('https://www.youtube.com', 'test')
