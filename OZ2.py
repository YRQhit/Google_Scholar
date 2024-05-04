from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# 创建WebDriver对象并分配给driver变量
driver = webdriver.Chrome()

# 打开网页
driver.get("https://scholar.google.com/citations?hl=zh-CN&user=rfMylpMAAAAJ&view_op=list_works&sortby=pubdate")

# 初始化计数器
i = 1
log_f = open("OZ.csv", "w+",encoding='utf-8')
log_f.write('year;jounral;title;url\n')
input("start")
while True:
    title = ""
    try:

        title = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(
            i) + "]/td[1]/a")
        title = title.text
    except:
        print("get title error")
    # print(title)

    # 作者
    # element = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[1]/td[1]/div[1]")
    # text = element.text
    # print(text)
    journal = ""
    # 期刊
    try:

        journal = driver.find_element(By.XPATH,
                                      "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(
                                          i) + "]/td[1]/div[2]")
        journal = journal.text
    except:
        print("error in jounral")
    # print(jounral)

    date = ""
    # date
    try:

        date = driver.find_element(By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(
            i) + "]/td[3]/span")
        date = date.text
    except:
        print("err in data")
    # print(data)

    # 点击进入下载页面
    # 显式等待直到元素可见
    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[" + str(i) + "]/td[1]/a")))
        # 点击元素
        element.click()
    except:
        print("err in element click")

    try:
        test_signl = driver.find_element(By.XPATH, "/html/body/div/div[7]/div[2]/div/div[2]/div[1]/div[1]")
    except:
        input("something error")

    href = ""
    #下载链接，统一格式
    try:
        href = driver.find_element(By.XPATH, "/html/body/div/div[7]/div[2]/div/div[1]/div[1]/div/a")
        href = href.get_attribute("href")
        # 打印 href 属性值
        # print(href)
    except:
        # print("这篇文章没有下载链接")
        pass





    if date == "" and journal == "" and title == "" and href == "":
        input("something error")
        i = i -1
    try:
        log_f.write(f'{date};{journal};{title};{href}\n')
        log_f.flush()
    except:
        print("error in ",i)
        # print("date",)
    i = i + 1
    # 返回到前一页
    driver.back()