from time import sleep
from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)


#ヘッダレスモードでファイルダウンロードを可能にする
def enable_download_in_headless_chrome(driver, download_dir):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
 
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    driver.execute("send_command", params)

#銘柄コード
meigara = 6806
#西暦
year = 2018

#ダウンロードしたいフォルダ
download_dir = './each_stock'+'/'+str(meigara)
 
#Chromeのオプション設定
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": download_dir
})
#ヘッダレスモード
options.add_argument('--headless')
 
browser = webdriver.Chrome('/Users/apple/python/chromedriver 2',options=options)
enable_download_in_headless_chrome(browser, download_dir)
browser.implicitly_wait(3)
 
current_url = "https://kabuoji3.com/stock/"
 

 
#指定年から2019年まで繰り返す
for i in range(year,2019):
    url = current_url + str(meigara) + "/" + str(i) + "/"
 
    # livedoorにアクセス
    browser.get(url)
 
    browser.find_element_by_name("csv").click()
 
    browser.find_element_by_name("csv").click()
    sleep(5)
    print("Download:" + url)
 
browser.quit()