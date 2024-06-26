from selenium import webdriver

def test_one(browser):
    browser.get("https://google.com")
    assert browser.title == "Google"