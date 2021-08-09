import json


def getOriJson(s, stepId, csrfToken, cookieNew):
    data3 = {"stepId": str(stepId),
             "instanceId": "",
             "admin": "false",
             "rand": "494.47470330858334",
             "width": "960",
             "lang": "zh",
             "csrfToken": csrfToken
             }
    header3 = {
        'Referer': 'http://e-office2.nuist.edu.cn/infoplus/form/' + str(stepId) + '/render',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Safari/537.36',
        'Origin': 'http://e-office2.nuist.edu.cn',
    }
    url3 = 'http://e-office2.nuist.edu.cn/infoplus/interface/render'
    requiredData = s.post(url3, headers=header3, data=data3, cookies=cookieNew, timeout=5)
    requiredDataObj = json.loads(requiredData.text)['entities'][0]['data']
    return requiredDataObj
