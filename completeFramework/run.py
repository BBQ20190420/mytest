import unittest
import os
import HTMLTestRunnerCN

#用例路径
case_path=os.path.join(os.getcwd(),'case')
print(case_path)

#存放报告路径
report_path=os.path.join(os.getcwd(),'report')
print(report_path)

def all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
    # runner=unittest.TextTestRunner()
    # runner.run(all_case())
    report_abspath=os.path.join(report_path,'result.html')
    print(report_abspath)
    fp=open(report_abspath,'wb')
    runner=HTMLTestRunnerCN.HTMLTestReportCN(stream=fp,description="执行结果",title="用例执行")
    runner.run(all_case())
    fp.close()