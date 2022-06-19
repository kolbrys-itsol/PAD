import ast

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import plotly.express as plot

if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # driver.get('https://vndb.org/v14014')
    # # novel_len = driver.find_element(by=By.XPATH, value='//*[@id="maincontent"]/div[2]/div[1]/table/tbody/tr[2]/td[2]').text
    # play_time = driver.find_element(by=By.XPATH,
    #                                 value="//*[contains(text(), 'Play time')]")
    # novel_len = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Play time')]/following-sibling::td")
    # # parent = play_time.find_element(by=By.XPATH, value='td')
    # print(novel_len.text.split()[0])
    # tags = driver.find_elements(by=By.XPATH, value='//*[@id="vntags"]//span//a')
    # tags_texts = []
    # for tag in tags:
    #     if tag.text != '':
    #         tags_texts.append(tag.text)
    #
    # print(tags_texts)
    df = pd.read_csv('data.csv')
    df['Count'] = df.Tags.transform(ast.literal_eval).str.len()
    # df = pd.Series(Counter(chain(*df.x))).sort_index().rename_axis('x').reset_index(name='f')
    print(df)
    # mask_nsc = df.Tags.apply(lambda t: 'No Sexual Content' in t)
    # # df1 = df[mask_nsc]
    # # print(df1.Id.count())
    # # print(df.Id.count())
    # # df.set_index('Id')['Tags'].groupby('Id').apply(list).apply(lambda t: 'No Sexual Content' in t)
    # df.agg(lambda t: 'No Sexual Content' in t)
    # print(df)


