import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# zad1

# wg. https://www.pap.pl/robots.txt, strona pozwala na web scraping

# zad2

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.pap.pl/')

    # a
    # driver.find_element_by_xpath("//div[@class='ok closeButton']").click()
    driver.find_element(by=By.XPATH, value="//div[@class='ok closeButton']").click()

    # b
    driver.maximize_window()

    # c
    driver.find_element(by=By.XPATH, value="//a[@href='http://www.pap.pl/en']").click()

    # d

    driver.find_element(by=By.XPATH, value="//a[@href='/en/business']").click()

    # e

    titles = driver.find_elements(by=By.CSS_SELECTOR,
                                  value='div.newsList div div.textWrapper h1 a, div.newsList div div.row ul li div.textWrapper h2 a')

    # for t in titles:
    #     print(t.text)

    # f

    images = driver.find_elements(by=By.CSS_SELECTOR,
                                  value='div.newsList div div.imageWrapper a img, div.newsList div div.row ul li div.imageWrapper a img')

    count = 1

    for i in images:
        response = requests.get(i.get_attribute('src'))
        with open(f'{count}.jpg', 'wb+') as o:
            o.write(response.content)
            count += 1

    # g

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # h

    driver.find_element(by=By.XPATH, value="//a[@title='Go to last page']").click()

    print(driver.find_element(by=By.XPATH,
                              value='/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[5]/a').text)

    driver.quit()
