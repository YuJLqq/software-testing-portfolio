import xlrd
from unittest_framework.test_def import *
filename=r"C:\Users\lenovo\Desktop\测试培训\order.xls"
excel=xlrd.open_workbook(filename)
#print(excel.sheets)
t=testD()
def readCase(sheetname):
    sheet=excel.sheet_by_name(sheetname)
    nr=sheet.nrows
    #print(nr)
    for i in range(1,nr):
        rv=sheet.row_values(i)#以列表的形式返回读取到的数据
        #print(rv)
        keyword,data,method,position,status=rv[2],rv[3],rv[4],rv[5],rv[6]
        #print(keyword,data,method,position,status)
        if keyword=="open":
            t.testOpen(data)
        elif keyword=="input":
            t.testInput(data, method, position)
        elif keyword=="click":
            t.testClick(method, position)
        elif keyword=="frame":
            t.testFrame(method, position, status)
        elif keyword=="sleep":
            t.testSleep(data)
        elif keyword=="select":
            t.testSelect(data, method, position, status)
        elif keyword=="js":
            t.testJs(data)
        elif keyword=="image":
            t.testImage(data, method, position)
            
readCase("login") 
readCase("order")   
