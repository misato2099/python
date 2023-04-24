from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import os
import time
import re
import random
from selenium.common.exceptions import NoSuchElementException

city = '' # city name
pattern = f'\d+{city}'
df = pd.read_csv('', encoding='utf-8-sig') # source file location
num_rows = df.shape[0]
lats = []
lons = []
adrmatch = []
rtadds = []
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome("CHROMEDRIVER LOCATION",chrome_options=option)
driver.get("https://www.google.com.tw/maps/")
sleep(3)

i = 1
start_time = time.time()

for address in df['ADDRESS COLUMN']: # column with address for searching
    time_start = time.time()
    driver.find_element_by_name("q").send_keys(address)
    driver.find_element_by_name("q").send_keys(Keys.RETURN)
    sleep(round(random.uniform(3,5),2))
    try:
        url = driver.current_url
        if not 'search' in url:
            lat = '2' + re.search(r'!3d2(.+?)!', url).group(1)
            try:
                lon = '12' + re.search(r'!4d12(.+?)!', url).group(1)
            except:
                lon = '12' + re.search(r'!4d12(.+?)\?', url).group(1)
            try:
                d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[10]/div[2]/div[2]/span[2]/span").get_attribute("textContent")
            except NoSuchElementException:
                try:
                    d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                except NoSuchElementException:
                    try:
                        d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                    except NoSuchElementException:
                        try:
                            d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[11]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                        except NoSuchElementException:
                            try:
                                d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                            except NoSuchElementException:
                                try:
                                    d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[13]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                                except:    
                                    d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[15]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
            rtadd = re.sub(pattern, city, d)
            # print(address)
            # print(rtadd)
            if address == rtadd:
                adrmatch.append('1')
            else:
                adrmatch.append('0')
            lats.append(lat)
            lons.append(lon)
            rtadds.append(rtadd)
            # print(rtadds)
            # print(lats)
            # print(lons)
        else:
            try:   
                d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/a")
                d.click()
                sleep(round(random.uniform(4,6),2))
                url = driver.current_url
            except NoSuchElementException:
                try:
                    d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/a")
                    d.click()
                    sleep(round(random.uniform(4,6),2))
                    url = driver.current_url
                except:
                    d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a")
                    d.click()
                    sleep(round(random.uniform(4,6),2))
                    url = driver.current_url
            lat = '2' + re.search(r'!3d2(.+?)!', url).group(1)
            try:
                lon = '12' + re.search(r'!4d12(.+?)!', url).group(1)
            except:
                lon = '12' + re.search(r'!4d12(.+?)\?', url).group(1)
            try:
                d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[10]/div[2]/div[2]/span[2]/span").get_attribute("textContent")
            except NoSuchElementException:
                try:
                    d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                except NoSuchElementException:
                    try:            
                        d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                    except NoSuchElementException:
                        try:   
                            d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[11]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                        except NoSuchElementException:
                            try:   
                                d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                            except NoSuchElementException:
                                try:   
                                    d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[13]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
                                except:
                                    d = driver.find_element_by_xpath("//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[15]/div[3]/button/div[1]/div[3]/div[1]").get_attribute("textContent")
            rtadd = re.sub(pattern, city, d)
            lats.append(lat)
            lons.append(lon)
            adrmatch.append('0')
            rtadds.append(rtadd)
            # print(rtadds)
            # print(lats)
            # print(lons)
    except:
        lats.append('NA')
        lons.append('NA')
        adrmatch.append('0')
        rtadds.append('Address cannot be located.')
        # print(rtadds)
        # print(lats)
        # print(lons)
        print(f'The {i} address cannot be located.')
    driver.find_elementby_name("q").clear()
    time_end = time.time()
    print(f'{i}/{num_rows} completed, total time spent {time_end-time_start:.2f} second(s).')
    i += 1

df.insert(loc=0, column='response_address', value=rtadds)
df.insert(loc=2, column='lat', value=lats)
df.insert(loc=3, column='lon', value=lons)
df.insert(loc=4, column='match', value=adrmatch)
df.to_csv('', index=False, encoding='utf-8-sig') # saving file location
driver.get("https://www.google.com.tw/maps/")
sleep(3)
driver.find_element_by_name("q").clear()
driver.quit()
total_seconds = time.time() - start_time
hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Total time spent: {int(hours)}hour(s){int(minutes)}minute(s){seconds:.2f}second(s)")
