from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# 创建WebDriver对象并分配给driver变量
driver = webdriver.Chrome()

# 打开网页
driver.get("https://scholar.google.com/citations?hl=zh-CN&user=0npZEX8AAAAJ&view_op=list_works&sortby=pubdate")

# 初始化计数器
i = 1

# 打开或创建 CSV 文件
with open("KB2.csv", "w", newline='') as log_f:
    # 写入 CSV 文件的表头
    log_f.write('year;journal;title;url\n')

    while i<100:
        try:
            # 等待标题元素可见
            title_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, f"/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[{i}]/td[1]/a")))

            # 找到标题元素
            title = title_element.text

            # 找到期刊元素
            journal = driver.find_element(By.XPATH,
                                          f"/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[{i}]/td[1]/div[2]").text

            # 找到日期元素
            date = driver.find_element(By.XPATH,
                                       f"/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[{i}]/td[3]/span").text

            # 点击进入下载页面
            title_element.click()

            url = ""
            try:
                # 点击进入下载页面
                driver.find_element(By.XPATH,
                                    f"/html/body/div/div[12]/div[2]/div/div[4]/form/div[1]/table/tbody/tr[{i}]/td[1]/a").click()
                # 等待下载链接元素可见
                download_link = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "/html/body/div/div[7]/div[2]/div/div[1]/div[1]/div/a")))
                url = download_link.get_attribute("href")
            except:
                print("there is no download url")

            # 写入 CSV 文件
            log_f.write(f'{date};{journal};{title};{url}\n')

            # 返回到前一页
            driver.back()

            # 增加计数器
            i += 1

        except Exception as e:
            print(f"Error at index {i}: {e}")

            # 滚动页面
            driver.execute_script(f"window.scrollTo(0, {i * 70});")

            # 等待下一页按钮可见
            next_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div/div[12]/div[2]/div/div[4]/form/div[2]/div/button/span/span[2]")))

            # 点击下一页
            next_button.click()

            # 重置计数器
            i = 1

# 关闭浏览器
driver.quit()
