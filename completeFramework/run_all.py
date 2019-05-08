import unittest
import os
#import HTMLTestRunnerCN
#from tomorrow import threads
import time
from BeautifulReport import BeautifulReport



#用例路径
case_path=os.path.join(os.getcwd(),'case')

#报告路径
report_path=os.path.join(os.getcwd(),'report')


def add_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
    return discover

# @threads(2)
# def run_case(all_case):
#     mytime=time.strftime('%Y%d%m%H%M%S',time.localtime(time.time()))
#     report_abspath=os.path.join(report_path,'report%s.html'%mytime)
#     fp=open(report_abspath,'wb')
#     runner=HTMLTestRunnerCN.HTMLTestReportCN(description='507测试报告',title='测试报告',tester='BBQ',stream=fp)
#     runner.run(all_case)
#     fp.close()

# if __name__ == '__main__':
#     cases=add_case()
#     for i,j in zip(cases,range(len(list(cases)))):
#         run_case(i)
def run(test_suite):
    result=BeautifulReport(test_suite)
    mytime=time.strftime('%Y%d%m%H%M%S',time.localtime(time.time()))

    result.report(description='测试报告',log_path=report_path,filename='report%s.html'%mytime)

if __name__ == '__main__':
    cases=add_case()
    print(cases)
    for i in cases:
        run(i)



