from selenium import webdriver
import time
class testD():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def testOpen(self,data):
        driver=self.driver
        driver.get(data)
        driver.maximize_window()
        driver.implicitly_wait(10)
    def testPosition(self,method,position):
        driver=self.driver
        for i in range(10):
            try:
                if method=="id":
                    ele=driver.find_element_by_id(position)
                elif method=="name":
                    ele=driver.find_element_by_name(position)
                elif method=="link":
                    ele=driver.find_element_by_link_text(position)
                elif method=="class":
                    ele=driver.find_element_by_class_name(position)
                elif method=="xpath":
                    ele=driver.find_element_by_xpath(position)
            except:
                time.sleep(1)
                if i==9:
                    import datetime
                    t=datetime.datetime.today().strftime("%Y%m%d%H%M%S")
                    driver.get_screenshot_as_file(r"D:\autotest\screenshot\%s.png"%(t))
                    return None
            else:
                return ele
    def testInput(self,data, method,position):
        ele=self.testPosition(method, position)
        if ele==None:
            print("输入框没有找到")
        else:
            ele.clear()
            ele.send_keys(data)
    def testClick(self,method,position):
        ele=self.testPosition(method, position)
        if ele==None:
            print("需要点击的元素没有找到")
        else:
            ele.click()
    def testFrame(self,method,position,status):
        driver=self.driver
        if status=="1":
            ele=self.testPosition(method, position)
            if ele==None:
                print("需要切换的子页面没有找到")
            else:
                if method=="id" or method=="name":
                    driver.switch_to.frame(position)
                else:
                    driver.switch_to.frame(ele)
        elif status=="2":
            driver.switch_to.parent_frame()
        elif status=="3":
            driver.switch_to.default_content()
        else:
            print("你输入的状态不合法")
            
    def testSleep(self,data):
        data=int(data)
        time.sleep(data)
    def testSelect(self,data,method,position,status):
        ele=self.testPosition(method, position)
        if ele==None:
            print("你需要操作的下拉框没有找到")
        else:
            from selenium.webdriver.support.select import Select
            s=Select(ele)
            if status=="index":
                data=int(data)
                s.select_by_index(data)
            elif status=="value":
                s.select_by_value(data)
            elif status=="text":
                s.deselect_by_visible_text(data)
            else:
                print("你的状态输入不合法")
    def testJs(self,data):
        driver=self.driver
        driver.execute_script(data)
    def testImage(self,data,method,position):
        ele=self.testPosition(method, position)
        time.sleep(2)
        if ele==None:
            print("上传图片的按钮没有找到")
        else:
            time.sleep(1)
            ele.send_keys(data)