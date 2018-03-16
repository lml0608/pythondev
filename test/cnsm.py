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
driver.get("https://passport.csdn.net/account/login?from=http://mp.blog.csdn.net/postlist")

# 获取页面名为 wrapper的id标签的文本内容
driver.find_element_by_id("username").send_keys('15112568068')

driver.find_element_by_id("password").send_keys('891212kb@')

