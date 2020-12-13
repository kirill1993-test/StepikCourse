import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language")


# Add parser from command line for ability to run test with different language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",help="Choose language")

@pytest.fixture
def browser(request):
    # Get language
    language = request.config.getoption("language")
    # Make variable Option class part
    options = Options()
    # Use language variable like user language
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # Print hello phrase
    print("\nstart chrome browser for test..")
    # Run browser with language settings
    browser = webdriver.Chrome(options=options)
    # Send browser in function
    yield browser
    # Say goodbye
    print("\nquit browser..")
    # Close browser
    browser.quit()

