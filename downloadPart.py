#读取csv文件
import csv
import requests
import os
# 打开 CSV 文件

import io
def download_pdf(save_path, pdf_name, pdf_url):
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    response = requests.get(pdf_url, headers=send_headers)
    bytes_io = io.BytesIO(response.content)
    pdf_name = pdf_name.replace(".", "")
    pdf_name = pdf_name.replace(" ", "")
    pdf_name = pdf_name.replace(":", "_")
    pdf_name = pdf_name.replace("…", "_")
    print(pdf_name)
    with open(save_path + "%s.PDF" % pdf_name, mode='wb') as f:
        f.write(bytes_io.getvalue())
        print('%s.PDF,下载成功！' % (pdf_name))

log_f = open("otherTypeFile.csv", "w+",encoding='utf-8')

with open('KB.csv', 'r', encoding='utf-8') as csvfile:
    # 创建 CSV reader 对象
    csvreader = csv.reader(csvfile)

    # 跳过第一行
    next(csvreader)

    # 读取第三列数据
    column_data = []
    for row in csvreader:
        # column_data.append(row[3])
        # print(row[0].split(";")[3])
    # print(column_data)
    #     print(row)
        # row = ['1990;Journal of Physics B: Atomic', ' Molecular and Optical Physics 23 (16)', ' L439;Near-threshold photoionisation of atomic barium from the (6s6p) 1Po1 state;https://www.researchgate.net/profile/Brendan_Mclaughlin/publication/232282141_Near-threshold_photoionisation_of_atomic_barium_from_the_6s6p_1Po1_state/links/09e41508122832020f000000.pdf']
        try:
            try:
                url = row[0].split(";")[-1]
                if  url.startswith("https") or url.startswith("http"):
                # if url.startswith("https") or url.startswith("http"):
                    print(url)
                    year = row[0].split(";")[0]
                    journal = row[0].split(";")[1]
                    title = row[0].split(";")[2].replace(".", "")
                    # print(journal)
                    # 发送 GET 请求下载 PDF 文件
                    # response = requests.get(url)

                    # 检查响应状态码是否为 200 (OK)
                    # print(response.status_code)
                    # if response.status_code == 200:
                    #     # 指定文件名
                    #     filename = "example.pdf"
                    #
                    #     # 写入 PDF 内容到本地文件
                    #     with open(filename, "wb") as f:
                    #         f.write(response.content)
                    #
                    #     print("PDF 文件已下载成功。")
                    #
                    #     # 可选：重命名文件
                    #     new_filename = "new_example.pdf"
                    #     os.rename(filename, new_filename)
                    #     print(f"PDF 文件已重命名为 {new_filename}。")
                    # else:
                    #     print("下载 PDF 文件失败。")
                    journalname = journal.split("_")[0].replace(".", "_")
                    journalpage = journal.split("_")[-1].replace(" ","")

                    pdf_name = str(year + "[" + journalname + "]" + journalpage +"_"+ title)
                    # print(pdf_name)

                    save_path = './KB/'

                    try:
                        download_pdf(save_path, pdf_name, url)
                    except:
                        print("下载失败")
                else:
                    year = row[0].split(";")[0]
                    journal = row[0].split(";")[1]
                    title = row[0].split(";")[2]
                    journalname = journal.split("_")[0].replace(".", "_")
                    journalpage = journal.split("_")[-1].replace(" ", "")
                    log_f.write(f'{year};{journalname};{journalpage};{title};{url}\n')
                    log_f.flush()
            except:
                pass


        except:
            pass

        



# url = "https://arxiv.org/pdf/2404.02985"
# #url2 = https://www.vamdc.org/wp-content/uploads/2014/10/VAMDC-USA-2014-Abstracts.pdf
# import io
# def download_pdf(save_path, pdf_name, pdf_url):
#     send_headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
#         "Connection": "keep-alive",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Accept-Language": "zh-CN,zh;q=0.8"}
#     response = requests.get(pdf_url, headers=send_headers)
#     bytes_io = io.BytesIO(response.content)
#     with open(save_path + "%s.pdf" % pdf_name, mode='wb') as f:
#         f.write(bytes_io.getvalue())
#         print('%s.pdf,下载成功！' % (pdf_name))
#
# from requests_html import HTMLSession
# if __name__ == '__main__':
#     save_path = './test/'
#     pdf_name = '2007年年度报告'
#     pdf_url = "https://arxiv.org/html/2311.03677v2"
#     download_pdf(save_path, pdf_name, pdf_url)
    # session = HTMLSession()
    # r = session.get(pdf_url)
    # print(r.html.html)


# from concurrent.futures import ThreadPoolExecutor
# import requests, argparse, re, os
# from bs4 import BeautifulSoup as Soup
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'
# }
#
#
# ## 设置命令行参数
# def setArgs():
#     parser = argparse.ArgumentParser(description="功能：下载pdf")
#     parser.add_argument("url", help="目标url")
#     parser.add_argument("-t", "--thread", help="最大的线程数。默认为3", default=3, type=int)
#     parser.add_argument("-f", "--filedir",
#                         help="文件保存的路径.默认为当前目录下的downloads文件夹.如果不存在，便自动新建",
#                         default="downloads")
#     return parser.parse_args()
#
#
# ## 获取所有pdf的url
# def getPdfUrl(root_url):
#     response = requests.get(root_url, headers=headers)
#     ## 如果requests没有从页面中获得字符编码，那么设置为utf-8
#     if "charset" not in response.headers:
#         response.encoding = "utf-8"
#     bsObj = Soup(response.text, "html.parser")
#     pdfs = bsObj.find_all("a", {"href": re.compile(r'.pdf$')})
#     ## 获得一个字典，key为pdf完整url，value为pdf名称
#     url_pdfName = {root_url[:root_url.rfind("/") + 1] + pdf["href"]: pdf.string for pdf in pdfs}
#     return url_pdfName
#
#
# ## 显示正在下载的pdf的名称
# def showPdf(pdf_name):
#     print(pdf_name + "...")
#
#
# ## 下载pdf
# def savePdf(url, pdf_name):
#     response = requests.get(url, headers=headers, stream=True)
#     ## 如果指定的文件夹，那么便新建
#     if not os.path.exists(FILE_DIR):
#         os.makedirs(FILE_DIR)
#     ## os.path.join(a,b..)如果a字符串没有以/结尾，那么自动加上\\。（windows下）
#     with open(os.path.join(FILE_DIR, pdf_name), "wb") as pdf_file:
#         for content in response.iter_content():
#             pdf_file.write(content)
#
#
# ## 设置要下载一个pdf要做的事情，作为线程的基本
# def downOne(url, pdf_name):
#     showPdf(pdf_name)
#     savePdf(url, pdf_name)
#     print(pdf_name + " has been downloaded!!")
#
#
# ## 开始线程
# def downPdf(root_url, max_thread):
#     url_pdfName = getPdfUrl(root_url)
#     with ThreadPoolExecutor(max_thread) as executor:
#         executor.map(downOne, url_pdfName.keys(), url_pdfName.values())
#
#
# def main():
#     ## 获得参数
#     args = setArgs()
#     ## 如果没有输入必须的参数，便结束，返回简略帮助
#     try:
#         global FILE_DIR
#         FILE_DIR = args.filedir
#         downPdf(args.url, args.thread)
#     except:
#         exit()
#
#
# if __name__ == "__main__":
#     main()
