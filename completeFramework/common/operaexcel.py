import xlrd
import os
#codeing:utf-8
class ExccelUtil():
    def __init__(self,excelpath,sheetname):
        """操作表"""
        #打开excel
        self.data=xlrd.open_workbook(excelpath)
        #打开单个表
        self.table=self.data.sheet_by_name(sheetname)
        #获取第一行
        self.keys=self.table.row_values(0).encode('utf-8')
        #获取总行数
        self.rowsNum=self.table.nrows
        #获取总列数
        self.colsNum=self.table.ncols


    def dict_data(self):
        """处理数据"""
        if self.rowsNum<=1:
            print("总行数小于1")
        else:
            r=[]
            j=1
            for i in range(self.rowsNum-1):
                s={}
                #从第二行开始读取
                values=self.table.row_values(j).encode('utf-8')
                for x in range(self.colsNum):
                    s[self.keys[x]]=values[x]
                    print(s)
                r.append(s)
                j+=1
            print(r)
            #return r
if __name__ == '__main__':
    datapath=os.path.dirname(os.getcwd())
    print(datapath)
    tablepath=os.path.join(datapath,'case/demo_data.xls')
    print(tablepath)
    mytable=ExccelUtil(tablepath,'qqsheet1')
    mytable.dict_data()
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print(os.getcwd())
    print(os.path.dirname(os.getcwd()))
    djjd=os.path.join()
