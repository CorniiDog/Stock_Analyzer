[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import web_scraping_utility`

Alternative Import Statement: `from toolbox.web_scraping_utility import *`

# >  function test_headless #

### [def test_headless(website: str, screenshot_path, screen_width: int = 1920, screen_height: int = 1080):](./../toolbox/web_scraping_utility.py#L9) 

Note

```python
    The screenshot will be saved as a .png file
    This function is built just to test the headless option of selenium.
```

Param

```python
ters
    ----------
    website: str
        The website to take a screenshot of
    screenshot_path: str
        The path to save the screenshot to
    screen_width: int
        The width of the screen to take the screenshot of
    screen_height: int
        The height of the screen to take the screenshot of
```

Return

```python
    None
```

Example

```python
    from toolbox import web_scraping_utility
    import os
    current_dir = os.getcwd()

    screenshot_path = os.path.join(current_dir, 'test')
    web_scraping_utility.test_headless('https://www.youtube.com', screenshot_path)
```

