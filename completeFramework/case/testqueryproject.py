import unittest
from completeFramework.common.parameter import fixPara
from completeFramework.common.apirequest import apirequest
requestNo=fixPara().getRequestNo()
# help(unittest)

class queryProject(unittest.TestCase):

    def setUp(self):
        print("测试开始")

    def testQuerypro(self):
        """测试标的查询功能"""
        req={
            "projectNo": "pro8aab9dd3d0674b17b22cdc539104744e"
         }
        resp=apirequest().directReq("QUERY_PROJECT_INFORMATION",req)
        self.assertEqual(resp['status'],"SUCCESS")

    def tearDown(self):
        print("测试结束")


if __name__ == '__main__':
    unittest.main()