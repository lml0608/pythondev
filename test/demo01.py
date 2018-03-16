from selenium import webdriver

import time

# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
#driver = webdriver.PhantomJS('/Library/phantomjs-2.1.1-macosx/bin/phantomjs')
driver = webdriver.PhantomJS()

# 如果没有在环境变量指定PhantomJS位置
# driver = webdriver.PhantomJS(executable_path="./phantomjs"))

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://www.baidu.com/")

# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text

# 打印数据内容
print(data)


# 打印页面标题 "百度一下，你就知道"
print(driver.title)

# 生成当前页面快照并保存
driver.save_screenshot("baidu.png")

# id="kw"是百度搜索输入框，输入字符串"长城"
time.sleep(5)

driver.find_element_by_id("kw").send_keys(u"长城")

# id="su"是百度搜索按钮，click() 是模拟点击
time.sleep(3)
driver.find_element_by_id("su").click()

# 获取新的页面快照
driver.save_screenshot("长城.png")

#打印网页渲染后的源代码
print(driver.page_source)

# 获取当前页面Cookie
print(driver.get_cookies())

time.sleep(3)

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)

# 输入框重新输入内容
driver.find_element_by_id("kw").send_keys("itcast")
time.sleep(3)

# 模拟Enter回车键
driver.find_element_by_id("su").send_keys(Keys.RETURN)
time.sleep(3)

# 清除输入框内容
driver.find_element_by_id("kw").clear()
time.sleep(3)

# 生成新的页面快照
driver.save_screenshot("itcast.png")
time.sleep(3)

# 获取当前url
print(driver.current_url)
time.sleep(3)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()
#
# # 关闭浏览器
driver.quit()
