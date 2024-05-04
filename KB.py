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
driver.get("https://scholar.google.com/citations?hl=zh-CN&user=0npZEX8AAAAJ&view_op=list_works&sortby=pubdate")

i = 200

import csv

# 打开或创建 CSV 文件
import os

# with open(log_f_name, "w+") as log_f:
log_f = open("KB.csv", "w+")
log_f.write('year;jounral;title;url\n')

# input("please load all the page, then enter")

# title = driver.find_element(By.XPATH,
#                             "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(i)  + "]/td[1]/a")
# text = title.text
# print(text)

while True:
    # print(i)
    try:
        try:
            try:
                title =""
                title = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr["+ str(i) +"]/td[1]/a")
                title = title.text
            except:
                print("get title error")
            # print(title)

            #作者
            # element = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/div[1]")
            # text = element.text
            # print(text)

            #期刊
            try:
                jounral = ""
                jounral = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr["+ str(i) +"]/td[1]/div[2]")
                jounral = jounral.text
            except:
                print("error in jounral")
            # print(jounral)


            #日期
            try:
                data = ""
                data = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr["+ str(i) +"]/td[3]/span")
                data = data.text
            except:
                print("err in data")
            # print(data)

            #点击进入下载页面
            # 显式等待直到元素可见
            try:
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr["+ str(i) +"]/td[1]/a")))
                # 点击元素
                element.click()
            except:
                print("err in element click")
        except:
            print("information err in" , i)
        #下载链接，统一格式
        try:
            href = driver.find_element(By.XPATH, "/html/body/div/div[7]/div[2]/div/div[1]/div[1]/div/a")
            href = href.get_attribute("href")
            # 打印 href 属性值
            print(href)
        except:
            print("这篇文章没有下载链接")
            href = ""

        #/html/body/div/div[6]/a/span[1]
        try:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[6]/a/span[1]")))
            # 点击元素
            element.click()
        except:
            print("click error")
            try:
                scroll_distance = 70 * i  # 向下滚动的像素数
                script = "window.scrollBy(0, {});".format(scroll_distance)
                driver.execute_script(script)
                clickbotton = driver.find_element(By.XPATH,
                                                  "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")

                clickbotton = driver.find_element(By.XPATH,
                                                  "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")
                clickbotton.click()
                time.sleep(3)
                element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[6]/a/span[1]")))
                # 点击元素
                element.click()
                print("solove the err")
            except:
                print("click err is still",i)
                pass

        try:
            scroll_distance = 70 * i  # 向下滚动的像素数
            script = "window.scrollBy(0, {});".format(scroll_distance)
            driver.execute_script(script)

            log_f.write('year,jounral,title,url\n')
            # print("data is",data,"jounral is", jounral,"title is", title,"href is", href)

        except:
            print("err in log")

        # log_f.write('{};{};{};{}\n'.format(data, jounral, title, href))
        # log_f.flush()
        if data=="" and jounral=="" and title=="" and href=="":
            # input("maybe is the check program")
            print("=================try again================")
            try:
                try:
                    title = ""
                    title = driver.find_element(By.XPATH,
                                                "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(
                                                    i) + "]/td[1]/a")
                    title = title.text
                except:
                    print("get title error")
                # print(title)

                # 作者
                # element = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/div[1]")
                # text = element.text
                # print(text)

                # 期刊
                try:
                    jounral = ""
                    jounral = driver.find_element(By.XPATH,
                                                  "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(
                                                      i) + "]/td[1]/div[2]")
                    jounral = jounral.text
                except:
                    print("error in jounral")
                # print(jounral)

                # 日期
                try:
                    data = ""
                    data = driver.find_element(By.XPATH,
                                               "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(
                                                   i) + "]/td[3]/span")
                    data = data.text
                except:
                    print("err in data")
                # print(data)

                # 点击进入下载页面
                # 显式等待直到元素可见
                try:
                    wait = WebDriverWait(driver, 10)
                    element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                           "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(
                                                                               i) + "]/td[1]/a")))
                    # 点击元素
                    element.click()
                except:
                    print("err in element click")
            except:
                print("information err in", i)
            # 下载链接，统一格式
            try:
                href = driver.find_element(By.XPATH, "/html/body/div/div[7]/div[2]/div/div[1]/div[1]/div/a")
                href = href.get_attribute("href")
                # 打印 href 属性值
                print(href)
            except:
                print("这篇文章没有下载链接")
                href = ""

            # /html/body/div/div[6]/a/span[1]
            try:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[6]/a/span[1]")))
                # 点击元素
                element.click()
            except:
                print("click error")
                try:
                    scroll_distance = 70 * i  # 向下滚动的像素数
                    script = "window.scrollBy(0, {});".format(scroll_distance)
                    driver.execute_script(script)
                    clickbotton = driver.find_element(By.XPATH,
                                                      "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")

                    clickbotton = driver.find_element(By.XPATH,
                                                      "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")
                    clickbotton.click()
                    time.sleep(3)
                    element = wait.until(
                        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[6]/a/span[1]")))
                    # 点击元素
                    element.click()
                    print("solove the err")
                except:
                    print("click err is still", i)
                    pass

            try:
                scroll_distance = 70 * i  # 向下滚动的像素数
                script = "window.scrollBy(0, {});".format(scroll_distance)
                driver.execute_script(script)

                # log_f.write('year,jounral,title,url\n')
                # print("data is",data,"jounral is", jounral,"title is", title,"href is", href)

            except:
                print("err in log")
            log_f.write('{};{};{};{}\n'.format(data, jounral, title, href))
            try:
                clickbotton = driver.find_element(By.XPATH,
                                                  "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")
                clickbotton.click()
                time.sleep(3)
            except:
                print("err in end click")
                pass
            try:
                for j in range(i / 100):
                    try:
                        scroll_distance = 70 * i  # 向下滚动的像素数
                        script = "window.scrollBy(0, {});".format(scroll_distance)
                        driver.execute_script(script)
                        clickbotton = driver.find_element(By.XPATH,
                                                          "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")
                        clickbotton.click()
                        time.sleep(3)
                        scroll_distance = 70 * i  # 向下滚动的像素数
                        script = "window.scrollBy(0, {});".format(scroll_distance)
                        driver.execute_script(script)
                    except:
                        print("err in end for")
                        pass

                print("success in " + str(i))
            except:
                print("err in the roll down")
            print("===========try  again  success====================")

        if data=="" and jounral=="" and title=="" and href=="":
            input("maybe is the check program")

        log_f.write('{};{};{};{}\n'.format(data, jounral, title, href))

        time.sleep(1)
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]
        #/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]
        try:
            clickbotton = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")
            clickbotton.click()
            time.sleep(3)
        except:
            print("err in end click")
            pass
        try:
            for j in range(i/100):
                try:
                    scroll_distance = 70 * i  # 向下滚动的像素数
                    script = "window.scrollBy(0, {});".format(scroll_distance)
                    driver.execute_script(script)
                    clickbotton = driver.find_element(By.XPATH,
                                                      "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")
                    clickbotton.click()
                    time.sleep(3)
                    scroll_distance = 70 * i  # 向下滚动的像素数
                    script = "window.scrollBy(0, {});".format(scroll_distance)
                    driver.execute_script(script)
                except:
                    print("err in end for")
                    pass

            print("success in " + str(i))
        except:
            print("last try")
        print("success in ",i)
        i = i + 1
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
        print("error is",i)
        i = i + 1
        pass



# 等待一段时间，确保文件下载完成

time.sleep(10)  # 根据你的网络速度和文件大小适当调整等待时间


# 关闭浏览器
driver.quit()