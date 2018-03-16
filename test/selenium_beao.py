import  unittest

from selenium import webdriver

from bs4 import BeautifulSoup

import time

class douyuSelenium(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.PhantomJS('/Library/phantomjs-2.1.1-macosx/bin/phantomjs')

    def testDouyu(self):

        self.driver.get('http://www.douyu.com/directory/all')

        while True:
            soup = BeautifulSoup(self.driver.page_source,'xml')

            titles = soup.find_all('h3',{'class':'ellipsis'})
            nums = soup.find_all('span',{'class':'dy-num fr'})

            for title,nums in zip(nums,titles):

                print(u"观众人数：" + nums.get_text().strip(),u"\t房间标题：" + title.get_text().strip())


            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break
            # 模拟下一页点击

            time.sleep(10)
            self.driver.find_element_by_class_name('shark-pager-next').click()

    # 退出时的清理方法
    def tearDown(self):
        print('加载完成...')
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()







