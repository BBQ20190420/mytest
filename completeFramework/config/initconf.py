'''
此文件为了方便书写conf.ini文件
'''
from configparser import ConfigParser
config=ConfigParser()
config['requrl']={
    "url":"http://172.19.60.92:8001/bha-neo-app/lanmaotech/",
    "redirecturl":'http://172.19.60.105:8090/lanmao-autotest-app/util/recorder/',

}

config['QA']={
    'platformNo':'6000003612'
}

config['USER']={
    'realname1':"包倩倩",
    'phone1':'18101309652',
    'idcardNo1':'421302199410278443',
    'bankcardNo1':'6214830165885301',
    'realname2':"梁慧琳",
    'phone2':'18811165327',
    'idcardNo2':'131081198912141047',
    'bankcardNo2':'6214920206176743'
}

config['GITUSER']={
    'user1': "BBQ20190420",
    'password1': "youareapig2012",
    'user2': "BBQ20190",
    'password2': "areapig2012",
    'user3': "BBQ420",
    'password3': "youare2012"
}




'''
将配置信息写入配置文件
'''
with open('conf.ini','w') as file:
    config.write(file)
