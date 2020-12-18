#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import *
import requests as rq
import os
from selenium import webdriver


# In[4]:
rootfolder = "D://videos//testdataset"



# In[5]:



# In[6]:


#male_celebrity_list = [ 'sad face man' , 'sad face man old' , 'sad face girl' , 'sad face baby' , 'angry face woman' , 'angry face man' , 'angry face boy' , 'angry face girl' , '']


# In[7]:


#print(len(male_celebrity_list))


# In[8]:

g_images_url = 'https://www.google.co.in/imghp?hl=en&tab=wi&authuser=0&ogbl'


# In[ ]:


import time
import urllib.request
def download_images(number,kword):
    rootfolder = "D://videos//testdataset"
    driver_path = 'D://python//chromedriver//chromedriver_win32//chromedriver.exe'
    driver = webdriver.Chrome(driver_path)
    keyword = []
    keyword.clear()
    keyword.append(kword)
    for i in range(1):
        count = 0
        os.chdir(rootfolder)
        name = keyword[i]
        driver.get(g_images_url)
        search_bar = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
        search_bar.send_keys(name)
        search_button = driver.find_element_by_xpath('//*[@id="sbtc"]/button')
        search_button.click()
        i = 0

        while i<7:  
            #for scrolling page
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    
            try:
                #for clicking show more results button
                driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
            except Exception as e:
                pass
            time.sleep(2)
            i+=1

        #parsing
        soup = BeautifulSoup(driver.page_source, 'html.parser')


        #scraping image urls with the help of image tag and class used for images
        img_tags = soup.find_all("img", class_="rg_i")
        #print(img_tags[1]['src'])
    
        os.mkdir(name)
        os.chdir(name)
        downloaded = 0
        for i in range(number):
            try:
                img = driver.get(img_tags[i]['src'])
                src = img_tags[i]['src']
                urllib.request.urlretrieve(src, name + str(count) + ".png")
                downloaded += 1
            except:
                #print('passed')
                pass
            count += 1
    #print('downloaded ' ,downloaded,'images of ',name)

    driver.close()
    


# In[ ]:




# In[ ]:





# In[ ]:




# In[ ]:




