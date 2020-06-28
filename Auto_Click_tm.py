import time
import datetime
from selenium import webdriver

driver = webdriver.Chrome()

def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get(website)
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
    print("请在20秒内完成扫码")
    time.sleep(20)
    driver.get(website) # 这里写你需要抢购商品的链接地址
    time.sleep(1)

def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > buytime:
            driver.find_element_by_link_text("立即购买").click()
            break;
        time.sleep(0.1)
    while True:
        try:
            if driver.find_element_by_link_text("提交订单"):
                driver.find_element_by_link_text("提交订单").click()
        except:
            time.sleep(1)
        print(now)
        time.sleep(0.1)

if __name__ == "__main__":
    buytime = input("请输入秒杀时间：时间格式（2020-11-12 00:00:00.000000）")
    website = input("请输入物品链接：")
    login()
    buy(buytime)
