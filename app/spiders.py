# coding: utf-8
"""Spiders."""

import requests
from bs4 import BeautifulSoup

url = "http://gkcf.jxedu.gov.cn/cjcx/LqQuerySelvet"
headers = {
    "Host": "gkcf.jxedu.gov.cn",
    "Connection": "keep-alive",
    "Content-Length": "93",
    "Cache-Control": "max-age=0",
    "Origin": "http://gkcf.jxedu.gov.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/" +
    "537.36 (KHTML, like Gecko) Ubuntu Chromium / 51.0.2704.79 Chrome " +
    "/ 51.0.2704.79 Safari / 537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9," +
    "image/webp,*/*;q=0.8",
    "Referer": "http://gkcf.jxedu.gov.cn/cjcx/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4"
}


def filters(code, pid):
    """Filter info by bs4."""
    payload = {
        'dmlx': 1,
        'va': 'UKywzivX',
        'year': '1636',
        'ct': '1',
        'code': code,
        'sfzh': pid,
        'yzm': 'QF1H78',
        'action.x': '65',
        'action.y': '4'
    }

    try:
        resp = requests.post(url, data=payload, headers=headers)
    except Exception:
        return {
            'data': {},
            'message': u'服务器繁忙',
            'status': 0
        }

    soup = BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', id='dlt')
    inner_tbs = table.find_all('table')

    if len(inner_tbs) > 1:
        info = inner_tbs[-1]
    else:
        return {
            'data': {},
            'message': u'暂未查到你的录取信息',
            'status': 0
        }

    temp = []
    all_tds = info.find_all('td')

    if all_tds:
        pass
    else:
        return {
            'data': {},
            'message': u'暂未查到你的录取信息',
            'status': 0
        }

    for i in all_tds:
        temp.append(i.get_text(strip=True).split(u'：')[-1])

    result = {
        'data': {},
        'message': u'获取录取信息成功',
        'status': 1
    }

    result['data'] = {
        'name': temp[0],
        'lqzt': temp[1],
        'ksh': temp[2],
        'zkzh': temp[3],
        'jhxzmc': temp[4],
        'lqzy': temp[5],
        'lqpc': temp[6],
        'lqkl': temp[7],
        'lqsj': temp[8],
        'jxdh': temp[9],
        'lqyx': temp[10],
    }

    return result
