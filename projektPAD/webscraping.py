import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get('https://vndb.org/v?f=&s=33w')
    df = pd.DataFrame(columns=['Name', 'Date', 'Rating', 'Popularity', 'Length', 'Tags'])
    df.index.name = 'Id'
    # użyłem pętli for żeby mieć kontrolę nad ilością pobieranych danych (strony po 50 rekordów każda)
    # pobieramy 1500 najpopularniejszych visual novels
    for i in range(30):
        table_rows = driver.find_elements(by=By.XPATH, value="//*[@id='maincontent']/form/div[3]/table/tbody//tr")
        for tr in table_rows:
            name = ''
            date = ''
            pop = ''
            rating = ''
            length = 'Not available'
            tags = []
            tds = tr.find_elements(by=By.TAG_NAME, value='td')
            for td in tds:
                if td.get_attribute('class') == 'tc_title':
                    name = td.text
                    td.find_element(by=By.TAG_NAME, value='a').click()
                    play_len = driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Play time')]/following-sibling::td")
                    if play_len:
                        length_raw = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Play time')]/following-sibling::td").text.split()
                        length = length_raw[0]
                        if length == 'Very':
                            length = 'Very ' + length_raw[1]
                    tags_texts = driver.find_elements(by=By.XPATH, value='//*[@id="vntags"]//span//a')
                    for tag in tags_texts:
                        if tag.text != '':
                            tags.append(tag.text)
                    driver.back()
                if td.get_attribute('class') == 'tc_rel':
                    date = td.text
                if td.get_attribute('class') == 'tc_pop':
                    pop = td.text
                if td.get_attribute('class') == 'tc_rating':
                    rating = td.text.split()[0]
            print(name, date, pop, rating, length, tags)
            df.loc[len(df.index)] = dict(Name=name, Date=date, Rating=rating, Popularity=pop, Length=length, Tags=tags)
            # wstrzymujemy działanie programu żeby uniknąć przekroczenia limitu requestów
            # przy 3 sekundach powinno zająć około 80 minut
            time.sleep(3)
        driver.find_element(by=By.XPATH, value="//*[@id='maincontent']/form/div[4]/ul[2]/li[1]/a").click()

    print(df)
    df.to_csv('data.csv')
