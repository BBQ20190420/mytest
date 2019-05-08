import os
from configparser import ConfigParser

#获取当前目录
cur_path=os.path.dirname(os.path.relpath(__file__))
#获取配置文件路径
configpath=os.path.join(cur_path,"conf.ini")
config=ConfigParser()
#获取配置文件
config.read(configpath)

# urlsections=config.sections()
# # print(urlsections[1])
initurl=config.get('requrl','url')
redirecturl=config.get('requrl','redirecturl')
platformNo=config.get('QA',"platformNo")
realname1=config.get('USER','realname1')
phone1=config.get('USER','phone1')
idcardNo1=config.get('USER','idcardNo1')
bankcardNo1=config.get('USER','bankcardNo1')

user1=config.get('GITUSER','user1')
pwd1=config.get('GITUSER','password1')
user2=config.get('GITUSER','user2')
pwd2=config.get('GITUSER','password2')
user3=config.get('GITUSER','user3')
pwd3=config.get('GITUSER','password3')

# print(initurl)
# # print(redirecturl)
# # print(platformNo)