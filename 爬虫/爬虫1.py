'''
Author: yao.xie 1595341200@qq.com
Date: 2024-03-01 16:08:04
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2024-03-01 18:32:59
FilePath: /python/爬虫/爬虫1.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import requests
import html2text
import json
from bs4 import BeautifulSoup
import re


def html_to_md(html_string):
    h = html2text.HTML2Text()
    h.ignore_links = True
    md_string = h.handle(html_string)

    return md_string


text_id = ['681781553']

import requests

cookies = {
    'SESSIONID': 'cNuLTluqkgBI16RDYQGFOFX6tIu4pjddtd4sBqRAAUd',
    'JOID': 'VVoSBE4clkCLUioXFxzxl2QmEeIAKsIq_yRDdWUpxCLZMRBcWDQ5o-5VKhIVB0cNYpZk7P0FJxXbyOZd12k83Ps=',
    'osd': 'VVgVAUIclEeOXioVEBn9l2YhFO4AKMUv8yRBcmAlxCDeNBxcWjM8r-5XLRcZB0UKZ5pk7voAKxXZz-NR12s72fc=',
    '_zap': 'f6ccf2bc-46aa-4070-8d62-5397f4dfe399',
    'd_c0': 'AABTrrmvNhePTvsuCtZDG3OSlSEm0GffC6Y=|1691586935',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1708596863,1708933559',
    '__snaker__id': 'FZ6885NOls3ngW23',
    'YD00517437729195%3AWM_NI': 'B0I0RBv9g7uAmfgV%2FjJ%2BqTc1W%2Bdg66iHUwV4PnK23dnw2o%2F2mdwhyntF0CA%2Bq9kCrhOmI%2FjIZcg%2B%2B7sfBS0aCdYfH34VzfAYQBsB5GFH9%2BQcXr4lHDszCiTS%2B4bIsb%2F4dGI%3D',
    'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee95e843b7b9b991dc3b98868eb7c45a839f9f87d8678292e1b2ef7e8cefabd2f22af0fea7c3b92a82f087d1d14ab6e7a9d8f84bafbaa9b7ae628af5bfb5e23b95f5ac88b53eab989b98d54094b285d3b270aea9fe90ae3aafbcb989fc66b89a00a4c421b3e7a5a4f1648db387d0e9439abda9ccaa3db1ba8eb4b36b81bc9787cb39f88ab687c453939ebda3b84d8698f7ccd4699caefc8dcb50b1a68d8ad759e9ecaeaaf26aedecaca8cc37e2a3',
    'YD00517437729195%3AWM_TID': 'oOSKREOEKJJEQVFVRVKBiVJ7Fw%2BX1L08',
    'z_c0': '2|1:0|10:1709202105|4:z_c0|80:MS4xazJBdElnQUFBQUFtQUFBQVlBSlZUWDlzeEdaUUtzOEtFVUJrMVVGa0lreW9jV2N4dlV3aDZBPT0=|830b577d6570c680407c4bf9acbffb1174f301afd5778bcf4f16bcd6c5a51452',
    'q_c1': '78794777bdcc4488ba2b8fc564d31a08|1692604362000|1692604362000',
    '_xsrf': '21725de9-731d-485d-82fc-715ec8dac90f',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1709287992',
    'KLBRSID': 'd6f775bb0765885473b0cba3a5fa9c12|1709288042|1709285907',
    'SESSIONID': '3Qjvtlgr7WgRa8NJI49t9A6MXXu6hOxbdqJBbr0CcVE',
    'JOID': 'U1oSB07vbyBuZY4qHuoI8YIRsN8P3ztJGRXhSG_cO0I_BbJnUR_lww5iiCwcbzoqCsqrdfn2Jjq5UV_1iijqu9s=',
    'osd': 'UF0QAE_saCJpZI0tHO0J8oUTt94M2DlOGBbmSmjdOEU9ArNkVh3iwg1liisdbD0oDcuocvvxJzm-U1j0iS_ovNo=',
    'tst': 'r',
    'BAIDU_SSP_lcr': 'https://www.baidu.com/link?url=m7Dvl5qAN8-HlsUxn78vW7OllNZcv7-TFWqKQP25S7a&wd=&eqid=cf7341e70008f3c30000000465e18cf1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://zhuanlan.zhihu.com/p/681781553',
    'Connection': 'keep-alive',
    # 'Cookie': 'SESSIONID=cNuLTluqkgBI16RDYQGFOFX6tIu4pjddtd4sBqRAAUd; JOID=VVoSBE4clkCLUioXFxzxl2QmEeIAKsIq_yRDdWUpxCLZMRBcWDQ5o-5VKhIVB0cNYpZk7P0FJxXbyOZd12k83Ps=; osd=VVgVAUIclEeOXioVEBn9l2YhFO4AKMUv8yRBcmAlxCDeNBxcWjM8r-5XLRcZB0UKZ5pk7voAKxXZz-NR12s72fc=; _zap=f6ccf2bc-46aa-4070-8d62-5397f4dfe399; d_c0=AABTrrmvNhePTvsuCtZDG3OSlSEm0GffC6Y=|1691586935; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1708596863,1708933559; __snaker__id=FZ6885NOls3ngW23; YD00517437729195%3AWM_NI=B0I0RBv9g7uAmfgV%2FjJ%2BqTc1W%2Bdg66iHUwV4PnK23dnw2o%2F2mdwhyntF0CA%2Bq9kCrhOmI%2FjIZcg%2B%2B7sfBS0aCdYfH34VzfAYQBsB5GFH9%2BQcXr4lHDszCiTS%2B4bIsb%2F4dGI%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee95e843b7b9b991dc3b98868eb7c45a839f9f87d8678292e1b2ef7e8cefabd2f22af0fea7c3b92a82f087d1d14ab6e7a9d8f84bafbaa9b7ae628af5bfb5e23b95f5ac88b53eab989b98d54094b285d3b270aea9fe90ae3aafbcb989fc66b89a00a4c421b3e7a5a4f1648db387d0e9439abda9ccaa3db1ba8eb4b36b81bc9787cb39f88ab687c453939ebda3b84d8698f7ccd4699caefc8dcb50b1a68d8ad759e9ecaeaaf26aedecaca8cc37e2a3; YD00517437729195%3AWM_TID=oOSKREOEKJJEQVFVRVKBiVJ7Fw%2BX1L08; z_c0=2|1:0|10:1709202105|4:z_c0|80:MS4xazJBdElnQUFBQUFtQUFBQVlBSlZUWDlzeEdaUUtzOEtFVUJrMVVGa0lreW9jV2N4dlV3aDZBPT0=|830b577d6570c680407c4bf9acbffb1174f301afd5778bcf4f16bcd6c5a51452; q_c1=78794777bdcc4488ba2b8fc564d31a08|1692604362000|1692604362000; _xsrf=21725de9-731d-485d-82fc-715ec8dac90f; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1709287992; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1709288042|1709285907; SESSIONID=3Qjvtlgr7WgRa8NJI49t9A6MXXu6hOxbdqJBbr0CcVE; JOID=U1oSB07vbyBuZY4qHuoI8YIRsN8P3ztJGRXhSG_cO0I_BbJnUR_lww5iiCwcbzoqCsqrdfn2Jjq5UV_1iijqu9s=; osd=UF0QAE_saCJpZI0tHO0J8oUTt94M2DlOGBbmSmjdOEU9ArNkVh3iwg1liisdbD0oDcuocvvxJzm-U1j0iS_ovNo=; tst=r; BAIDU_SSP_lcr=https://www.baidu.com/link?url=m7Dvl5qAN8-HlsUxn78vW7OllNZcv7-TFWqKQP25S7a&wd=&eqid=cf7341e70008f3c30000000465e18cf1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
}

response = requests.get('https://www.zhihu.com/people/fengzhe_love', cookies=cookies, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
title = soup.find('title').text
res = re.findall('\d+', response.text)

for i in res:
    print(i)
    with open(f"./爬虫/{title}.html", 'w', encoding='utf-8') as f:
        f.write(response.text)
