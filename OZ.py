from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# 创建WebDriver对象并分配给driver变量
driver = webdriver.Chrome()

# 使用driver来访问WebDriver的功能
driver.get("https://scholar.google.com/citations?hl=zh-CN&user=rfMylpMAAAAJ&view_op=list_works&sortby=pubdate")

i = 201

import csv

# 打开或创建 CSV 文件
import os

# with open(log_f_name, "w+") as log_f:
log_f = open("OZ.csv", "w+")
log_f.write('year;jounral;title;url\n')

input("please load all the page, then enter")

# title = driver.find_element(By.XPATH,
#                             "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(i)  + "]/td[1]/a")
# text = title.text
# print(text)

while True:
    # print(i)
    try:
        # print("start")
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/a/text()
        #title
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/a
        title = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr["+ str(i) +"]/td[1]/a")
        title = title.text
        print(title)

        #作者
        # element = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/div[1]")
        # text = element.text
        # print(text)

        #期刊
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/a/text()
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/div[2]/text()
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/div[2]/text()
        jounral = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr["+ str(i) +"]/td[1]/div[2]")
        jounral = jounral.text
        print(jounral)


        #日期
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[3]/span
        data = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr["+ str(i) +"]/td[3]/span")
        data = data.text
        print(data)

        #点击进入下载页面
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/a
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[2]/td[1]/a
        # 显式等待直到元素可见
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr["+ str(i) +"]/td[1]/a")))
        # 点击元素
        element.click()

        #下载链接，统一格式
        #//*[@id="gsc_oci_title_gg"]/div/a
        #/html/body/div/div[7]/div[2]/div/div[1]/div[1]/div/a
        #/html/body/div/div[7]/div[2]/div/div[1]/div[1]/div/a
        #/html/body/div/div[7]/div[2]/div/div[1]/div[1]/div/a
        try:
            href = driver.find_element(By.XPATH, "/html/body/div/div[7]/div[2]/div/div[1]/div[1]/div/a")
            href = href.get_attribute("href")
            # 打印 href 属性值
            print(href)
        except:
            print("这篇文章没有下载链接")
            href = ""

        #/html/body/div/div[6]/a/span[1]
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[6]/a/span[1]")))
        # 点击元素
        element.click()

        try:
            scroll_distance = 70 * i  # 向下滚动的像素数
            script = "window.scrollBy(0, {});".format(scroll_distance)
            driver.execute_script(script)

            #log_f.write('year,jounral,title,url\n')
            log_f.write('{};{};{};{}\n'.format(data, jounral, title, href))
            log_f.flush()
        except:
            print("error here")

        i = i + 1
        time.sleep(1)
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]
        try:
            clickbotton = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")
            clickbotton.click()
            time.sleep(3)
        except:
            pass

        for j in range(i/100):
            try:
                scroll_distance = 100 * i  # 向下滚动的像素数
                script = "window.scrollBy(0, {});".format(scroll_distance)
                driver.execute_script(script)
                clickbotton = driver.find_element(By.XPATH,
                                                  "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")
                clickbotton.click()
                time.sleep(3)
            except:
                pass
    except:
        try:
            scroll_distance = 70 * i  # 向下滚动的像素数
            script = "window.scrollBy(0, {});".format(scroll_distance)
            driver.execute_script(script)
            clickbotton = driver.find_element(By.XPATH,
                                              "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")

            clickbotton = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")
            clickbotton.click()
            time.sleep(3)
        except:
            pass
        input("please load the page")
        print("error in",i)
        i = i + 1
        pass



# 等待一段时间，确保文件下载完成

time.sleep(10)  # 根据你的网络速度和文件大小适当调整等待时间


# 关闭浏览器
driver.quit()