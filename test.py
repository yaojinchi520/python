from selenium import webdriver
import time
# 封装查找页面输入框元素的和查找页面点击按钮元素，并赋值或者做点击事件
def findDomClick(xpath,id):
    isLoading = True
    # 确认loading是否存在
    while isLoading:
        try:
            browser.find_element_by_xpath("//div[@id='loading']")
        except:
            print(xpath+"loading结束了")
            isLoading = False
    isFind = False
    a = 0
    # 确认要找的元素是否已经加载
    while not isFind:
        try:
            a += 1
            clickDom = browser.find_element_by_xpath(xpath)
            isFind = True
        except:
            print("执行了 "+str(a)+" 次循环，本次要找元素："+xpath)
    # 确认要找的元素是否被禁用
    while not clickDom.is_enabled():
        print("休眠前")
        print(clickDom.is_enabled())
        time.sleep(0.5)
        print("休眠后")
        print(clickDom.is_enabled())
    if id:
        # 调用该方法如果传递了第二个参数，说明是找输入框，将值赋值给输入框
        clickDom.send_keys(id)
    else:
        # 没有第二个值，则说明找的是点击按钮，直接执行点击操作
        clickDom.click()
# 打开浏览器
browser = webdriver.Chrome()
# 将浏览器放大到全屏
browser.maximize_window()
url = "http://b9.hnzls.com:2008"
# 打开具体页面
browser.get(url)
# 登录相关输入
browser.find_element_by_id("TextCompanyCode").send_keys("x00226")
browser.find_element_by_id("TextLoginName").send_keys('zlsmd01')
browser.find_element_by_id("TextPassWord").send_keys('0')
# 登录
browser.find_element_by_id("buttonLogin").click()
# 登录后停顿等待工作台
time.sleep(5)
print("等待1.5秒后")
# 到门店
findDomClick("//ul[@id='topMenuList']/li[@data-id='StoreMgr']",False)
# 到门店POS
findDomClick("//a[@title='门店POS']",False)
# 找到门店所在的iframe框架
iframeDom = browser.find_element_by_xpath('//iframe[@id="fragment-iframe-StoreSaleView"]')
# 进入门店POS框架页面内
browser.switch_to.frame(iframeDom)
# 门店POS框架页面内操作
findDomClick("//input[@id='txtPhone']",15838205002)
findDomClick("//input[@id='btnQueryByPhone']",False)
findDomClick("//input[@id='txtProduct']","八")
findDomClick("//input[@id='btnQueryByProduct']",False)
# 确认销售员是否已被赋值
salesMan = ""
while salesMan=="":
    salesMan = browser.find_element_by_xpath('//input[@id="ddlSalesMan"]').get_attribute("title")
print("----------------------会不会在这循环---------------------------")
# 点击结算按钮
findDomClick("//input[@id='btnSettlement']",False)
# 跳出当前iframe框架，回到默认页面
browser.switch_to.default_content()
time.sleep(2)
# 从默认页面找当前弹出的iframe框架页面
iframeDomBtn = browser.find_element_by_xpath('//iframe[@id="dialog_content_iframe"]')
# 进入当前弹出的iframe框架页面
browser.switch_to.frame(iframeDomBtn)
# 进行相关操作
findDomClick("//input[@id='btnSure']",False)
findDomClick("//input[@id='btnSave']",False)
# 操作完再次跳回默认页面
browser.switch_to.default_content()
time.sleep(2)
# 找到弹窗按钮执行相关操作
findDomClick("//input[@value='确定']",False)
time.sleep(10)
browser.quit()