# -*- coding: UTF-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import json
import getIpdp
import formDataTrans
import getOriJson

try:
    with open('./Account.txt', 'r') as g:
        lines = g.readlines()
        username = lines[0]
        password = lines[1]
        print(username)
        print(password)
except FileNotFoundError as e:
    print("没有找到Paste_To_Me.txt文件，请查看Github Readme！")
    exit(0)

# 运行前检查服务器正常
print(time.strftime('%Y-%m-%d %H:%M:%S'))
getIpdp.checkServer()

s = requests.Session()
url = 'http://e-office2.nuist.edu.cn/infoplus/form/XNYQSB/start'
cookies = dict(iPlanetDirectoryPro=getIpdp.getIpdp(username, password))
r1 = s.get(url, cookies=cookies, timeout=5)
cookieNew = r1.cookies
# 填写页面的cookie
htmlTextOri = r1.text
html = BeautifulSoup(htmlTextOri, 'lxml')
tar1 = str(html.find_all('meta')[3])
csrfToken = tar1.split('"')[1]
url2 = 'http://e-office2.nuist.edu.cn/infoplus/interface/start'
data2 = {'idc': 'XNYQSB',
         'release': '',
         'csrfToken': csrfToken,
         'formData': '{"_VAR_URL":"http://e-office2.nuist.edu.cn/infoplus/form/XNYQSB/start","_VAR_URL_Attr":"{}"}'
         }
header2 = {'Referer': 'http://e-office2.nuist.edu.cn/infoplus/form/XNYQSB/start',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.198 Safari/537.36',
           'Origin': 'http://e-office2.nuist.edu.cn',
           }
r2 = s.post(url2, data=data2, cookies=cookieNew,
            headers=header2, timeout=5)
targetUrl = json.loads(r2.text)['entities'][0]
stepId = int(targetUrl.split('/')[5])
t2 = int(time.time())
# UTC时间戳
requiredDataObj = getOriJson.getOriJson(s, stepId, csrfToken, cookieNew)
formData2Obj = formDataTrans.formDataTrans(requiredDataObj)

postData2 = {
    'actionId': 1,
    'formData': json.dumps(formData2Obj),
    'remark': '',
    'rand': 36.72482730892129,
    'nextUsers': '{}',
    'stepId': stepId,
    'timestamp': t2,
    'boundFields': 'fieldCXXXjtgjbc,fieldMQJCRxh,fieldCXXXsftjhb,fieldSTQKqt,fieldSTQKglsjrq,fieldYQJLjrsfczbldqzt,'
                   'fieldCXXXjtfsqtms,fieldCXXXjtfsfj,fieldJBXXjjlxrdh,fieldJBXXxm,fieldJBXXjgsjtdz,'
                   'fieldCXXXsftjhbss,fieldSTQKfrtw,fieldMQJCRxm,fieldCXXXsftjhbq,fieldSTQKqtms,fieldCXXXjtfslc,'
                   'fieldJBXXlxfs,fieldJBXXxb,fieldCXXXjtfspc,fieldYQJLsfjcqtbl,fieldCXXXssh,fieldJBXXgh,fieldCNS,'
                   'fieldYC,fieldSTQKfl,fieldCXXXsftjwh,fieldCXXXfxxq,fieldSTQKdqstzk,fieldSTQKhxkn,fieldSTQKqtqksm,'
                   'fieldFLid,fieldYQJLjrsfczbl,fieldJBXXjjlxr,fieldCXXXfxcfsj,fieldMQJCRcjdd,fieldSQSJ,'
                   'fieldSTQKfrsjrq,fieldSTQKks,fieldJBXXcsny,fieldSTQKgm,fieldJBXXnj,fieldCXXXjtzzq,fieldJBXXJG,'
                   'fieldCXXXdqszd,fieldCXXXjtzzs,fieldSTQKfx,fieldSTQKfs,fieldCXXXjtfsdb,fieldCXXXcxzt,'
                   'fieldCXXXjtfshc,fieldCXXXjtjtzz,fieldCXXXsftjhbs,fieldJBXXsfzh,fieldSTQKsfstbs,fieldCXXXcqwdq,'
                   'fieldJBXXfdygh,fieldJBXXjgshi,fieldJBXXfdyxm,fieldWXTS,fieldCXXXjtzz,fieldJBXXjgq,'
                   'fieldCXXXjtfsqt,fieldJBXXjgs,fieldSTQKfrsjsf,fieldSTQKglsjsf,fieldJBXXdw,fieldCXXXsftjhbjtdz,'
                   'fieldMQJCRlxfs',
    'csrfToken': csrfToken,
    'lang': 'zh',
}
url3 = 'http://e-office2.nuist.edu.cn/infoplus/interface/doAction'
header3 = {'Referer': 'http://e-office2.nuist.edu.cn/infoplus/form/' + str(stepId) + '/render',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.198 Safari/537.36',
           'Origin': 'http://e-office2.nuist.edu.cn',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           }
r3 = s.post(url3, data=postData2, cookies=cookieNew,
            headers=header3, timeout=5)
if json.loads(r3.text)['ecode'] == 'SUCCEED':
    print('成功！')
    # 你可以使用SERVER酱一类的云推送服务来将打卡结果推送到手机上！
    # r4 = s.get("https://sctapi.ftqq.com/xxxxx.send?title=自动健康日报成功！")
else:
    print('打卡失败，' + r3.text)
    # r4 = s.get("https://sctapi.ftqq.com/xxxxx.send?title=自动健康日报成失败！&desp="+r3.text)
