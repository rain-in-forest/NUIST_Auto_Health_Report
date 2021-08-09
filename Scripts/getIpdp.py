from datetime import time

import execjs
import requests
from bs4 import BeautifulSoup


def getIpdp(username, password):
    url = 'https://authserver.nuist.edu.cn/authserver/login?service=http%3A%2F%2Fauthserver.nuist.edu.cn%2Fauthserver' \
          '%2Findex.do '
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Safari/537.36',
        'DNT': '1',
        'Host': 'authserver.nuist.edu.cn',
        'Origin': 'https://authserver.nuist.edu.cn',
        'Referer': 'https://authserver.nuist.edu.cn/authserver/login?service=http%3A%2F%2Fauthserver.nuist.edu.cn'
                   '%2Fauthserver%2Findex.do '
    }
    s = requests.Session()
    r = s.get(url, timeout=100)
    htmlTextOri = r.text
    html = BeautifulSoup(htmlTextOri, 'lxml')
    pwdEncryptSalt = html.find(id='pwdEncryptSalt')['value']
    execution = html.find(id='execution')['value']
    cookies = r.cookies
    # print(cookies.values())
    with open('./Scripts/encrypt.js', 'r', encoding="utf-8") as f:
        script = f.read()
    encrypt = execjs.compile(script)
    encodedPassword = encrypt.call(
        'encryptPassword', password, pwdEncryptSalt)
    # print(encodedPassword)
    data = {
        'username': username,
        'password': encodedPassword,
        'captcha': '',
        '_eventId': 'submit',
        'cllt': 'userNameLogin',
        'lt': '',
        'execution': execution,
    }
    r2 = s.post(url, data=data, cookies=cookies,
                headers=header, timeout=100, allow_redirects=False)
    targetCookie = r2.cookies.get_dict()['iPlanetDirectoryPro']
    return targetCookie


def checkServer():
    try:
        testSvr = requests.get('http://e-office2.nuist.edu.cn/', timeout=100).text
        testSvr = requests.get('http://authserver.nuist.edu.cn', timeout=100).text
    except requests.exceptions.RequestException as e:
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        print("学校服务器崩了，请联系辅导员")
        exit(0)
