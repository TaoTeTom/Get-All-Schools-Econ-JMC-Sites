


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from Selenium_JMC_Functions import get_url_df


df = pd.read_excel(r'C:\Users\15the\Documents\NLP Projects\Selenium_JMC\JMC_Urls.xlsx')
school_url_df = get_url_df(df)



#print(df)
#
# def get_url_df(df):
#     # convert data frame to list
#     school_name_list = df.values.tolist()
#     # print(school_name_list)
#
#     # get all urls from each school on list
#     jmc_urls = get_jmc_urls(school_name_list)
#     print(jmc_urls)
#     school_url_list = list(zip(school_name_list, jmc_urls))
#
#     school_ur_df = pd.DataFrame(school_url_list, columns=['School', 'Url'])
#
#     school_ur_df.to_csv('School_JMC_URLs.csv')
#     return school_ur_df




# #convert data frame to list
# school_name_list= df.values.tolist()
# #print(school_name_list)
#
# #get all urls from each school on list
# jmc_urls= get_jmc_urls(school_name_list)
# print(jmc_urls)
# school_url_list = list(zip(school_name_list, jmc_urls))
#
# school_ur_df = pd.DataFrame(school_url_list, columns=['School', 'Url'])
#
# school_ur_df.to_csv('School_JMC_URLs.csv')

# This is done to structure the string
# into search url.(This can be ignored)
# school = ['Johns Hopkins']
# print(school[0])
# search_string = ('https://www.google.com/search?q='+
#                  school[0]+
#                  '+econ+job+market+candidates&rlz=1C1CHBD_enUS811US811&oq=harvard&aqs='
#                  'chrome.0.69i59j46i433i512j69i59j0i433i512l2j69i60l3.1242j0j4&sourceid=chrome&ie=UTF-8')
#
# browser = webdriver.Chrome()
# matched_elements = browser.get(search_string)
# results = browser.find_elements(By.CSS_SELECTOR, 'div.g')
# link = results[0].find_element(By.TAG_NAME, "a")
# href = link.get_attribute("href")
#
# print("hihihihih")
# harvard = get_first_search_result(search_string)
# print(harvard)
# print(href)


