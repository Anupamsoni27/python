import pandas as pd
from selenium import webdriver
import time
df = pd.read_csv("PLATTS GI & GJ - GDATAL-5973.csv")
temp_list = list(df["SYMBOL"])
temp_list2 = []
for symbol in temp_list:
    start_date =""
    end_date = ""
    try:
        print("Seaching : "+ symbol)
        driver = webdriver.Chrome("C:\\Python36-32\\selenium\\webdriver\\chromedriver.exe")
        url= "https://www.spglobal.com/platts/en/our-methodology/symbol-page-directories"
        driver.maximize_window()
        driver.get(url)
        search = driver.find_element_by_id("txtSymbol")
        search.send_keys(symbol)
        driver.find_element_by_id("btnSymbol").click()
        time.sleep(1)
        driver.find_element_by_xpath("""//*[@id="symbolResult"]/div/ul/li/a""").click()
        # print(driver.find_element_by_xpath("""//*[@id="5tnhj0-acc-menu"]/li[11]/div[2]/h5""").text)
        start_date = driver.find_element_by_xpath("""//*[@id="5tnhj0-acc-menu"]/li[11]/div[2]/h5""").text
        # print(driver.find_element_by_xpath("""//*[@id="5tnhj0-acc-menu"]/li[12]/div[2]/h5""").text)
        end_date = driver.find_element_by_xpath("""//*[@id="5tnhj0-acc-menu"]/li[12]/div[2]/h5""").text
        row  = symbol,start_date,end_date
        print(row)
        temp_list2.append(row)
        driver.close()
    except:
        pass

    # mySelect = Select(driver.find_element_by_xpath("""//*[@id="txtSymbol"]"""))
    # print(mySelect)
df2 = pd.DataFrame(temp_list2, columns=["Symbol","Start date", "End date"])
df2.to_csv("output.csv",index=False)
