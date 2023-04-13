# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
 
flag = 0
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
                         })
 
def autoFillSpace(username, sid, dept, phone):
    browser.get(url)  # 获取问卷星 url
    time.sleep(0.1)
    # # 您的姓名
    try:
        browser.find_element(By.ID, 'q1').send_keys(username)  # 这个传入的参数不能跟上面的对象重复
    #
    except NoSuchElementException:
        return
    # # 学号
    browser.find_element(By.ID, 'q2').send_keys(sid)
 
 	# # 所在学院
    browser.find_element(By.ID, 'q3').send_keys(dept)

    # # 电话号码
    browser.find_element(By.ID, 'q4').send_keys(phone)
 
    # # 提交
#    try:
    ele = browser.find_element(By.ID, 'ctlNext')
#    except NoSuchElementException:
#        ele = browser.find_element(By.ID, 'submitbtn')
    ele.click()
    time.sleep(0.4)
    #
    # # 模拟点击智能验证按钮
#    browser.find_element(By.XPATH, "//button[text()='确认']").click()
#    browser.find_element(By.XPATH, "//div[@id='captcha']").click()
    try:
        element = driver.find_element_by_css_selector("#alert_box > div:nth-child(2) > div:nth-child(2) > button")
        element.click()
        time.sleep(0.5)
        yanz = driver.find_element_by_id("rectMask")
        yanz.click()
        time.sleep(2)
    except:
        pass
    return 1
 
if __name__ == '__main__':
	# 每次抢票都要修改
    # https://www.wjx.top/vm/OTRH5Yo.aspx
    # https://www.wjx.top/vm/mFw0owk.aspx
#        https://www.wjx.cn/vm/m750otL.aspx
#    url = 'https://www.wjx.cn/vm/OtSYCE8.aspx'  # 问卷星的链接
    url = 'https://www.wjx.top/vm/OTRH5Yo.aspx'
#    inp = input("输入问卷链接(回车为默认)：")
#    if(inp != ""):
#    	url = inp

    username = u'郑强'  # 您的姓名
    sid = '2201213416'  # 学号
    phone = '18844128167'  # 电话号码
    dept = u'城市与环境学院'  # 所在学院
    cnt = 0
    while True:
        flag = autoFillSpace(username, sid, phone, dept)
        if flag == 1:
            time.sleep(10)
            browser.close()
            break
        else:
            cnt += 1
            print(f'时间未到{cnt + 1}')


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import *
#import time
#
#flag = 0
#option = webdriver.ChromeOptions()
#option.add_experimental_option('excludeSwitches', ['enable-automation'])
#option.add_experimental_option('useAutomationExtension', False)
#browser = webdriver.Chrome(options=option)
#browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
#                        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
#                         })
#
#def autoFillSpace(username, sid, dept, phone):
#    browser.get(url)  # 获取问卷星 url
#    time.sleep(0.1)
#    # # 您的姓名
#    try:
#        browser.find_element(By.ID, 'q1').send_keys(username)  # 这个传入的参数不能跟上面的对象重复
#    #
#    except NoSuchElementException:
#        return
#    # # 学号
#    browser.find_element(By.ID, 'q2').send_keys(sid)
#
#     # # 所在学院
#    browser.find_element(By.ID, 'q3').send_keys(dept)
#
#    # # 电话号码
#    browser.find_element(By.ID, 'q4').send_keys(phone)
#
#    # # 提交
#    try:
#        ele = browser.find_element(By.ID, 'ctlNext')
#    except NoSuchElementException:
#        ele = browser.find_element(By.ID, 'submit_button')
#    ele.click()
#    time.sleep(0.1)
#    #
#    # # 模拟点击智能验证按钮
#    browser.find_element(By.XPATH, "//button[text()='确认']").click()
#    browser.find_element(By.XPATH, "//div[@id='captcha']").click()
#    return 1
#
#if __name__ == '__main__':
#    # 每次抢票都要修改
#    url = 'https://www.wjx.cn/vm/m750otL.aspx'  # 问卷星的链接
#    inp = input("输入问卷链接(回车为默认)：")
#    if(inp != ""):
#        url = inp
#
#    username = u'郑强'  # 您的姓名
#    inp = input("输入个人姓名：")
#    if(inp != ""):
#        username = inp
#
#    sid = '2201213416'  # 学号
#    inp = input("输入个人学号：")
#    if(inp != ""):
#        sid = inp
#
#    phone = '18844128167'  # 电话号码
#    inp = input("输入个人手机：")
#    if(inp != ""):
#        phone = inp
#
#    dept = u'城市与环境学院'  # 所在学院
#    print(type(dept))
#
#    inp = input("输入个人学院：")
#    if(inp != ""):
#        dept = inp
#
#    print(url, username, type(username), sid, phone, dept)
#    cnt = 0
#    while True:
#        flag = autoFillSpace(username, sid, dept, phone)
#        if flag == 1:
#            time.sleep(10)
#            break
#        else:
#            cnt += 1
#            print(f'时间未到{cnt + 1}')
