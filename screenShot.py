from selenium import webdriver
import urllib.parse

# uncomment to hide browser =================
# options = webdriver.ChromeOptions()
# options.add_argument("headless")

browser = webdriver.Chrome(
    "../chromedriver_win32/chromedriver")  # , chrome_options=options) ======================

carbon = "https://carbon.now.sh/?bg=rgba(107%2C65%2C163%2C1)&t=material&wt=none&l=python&ds=true&dsyoff=14px&dsblur=68px&wc=false&wa=true&pv=200px&ph=100px&ln=false&fm=Fira%20Code&fs=14px&lh=143%25&si=false&es=4x&wm=false?code={code}"


def shot(title, cs):
    code = urllib.parse.quote_plus(cs)

    browser.get(code)

    input = browser.find_element_by_xpath(
        '//*[@id="export-container"]/div[1]/div[1]/div/div[1]')
    input.click()
    input.send_keys(cs)
    print(input.text)
