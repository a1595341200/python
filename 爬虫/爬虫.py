'''
Author: yao.xie 1595341200@qq.com
Date: 2024-03-01 16:08:04
LastEditors: yao.xie 1595341200@qq.com
LastEditTime: 2024-03-01 18:12:30
FilePath: /python/爬虫/爬虫.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import requests
import html2text
import json
from bs4 import BeautifulSoup


def html_to_md(html_string):
    h = html2text.HTML2Text()
    h.ignore_links = True
    md_string = h.handle(html_string)
    return md_string


text_id = ['681781553']

cookies = {
    '__snaker__id': 'JLQ9VlhGktmaN3Cd',
    'SESSIONID': 'ByMOaO5jzKuQ8QY94GP7QuIaBtGyDHF6WylAzbEwVp9',
    'JOID': 'WlkcA0PKzFZUbx6oNMKlgL8YLVMi8JU1Kht7x0_9kjkPBibvdjNBtjlmH6k14JUPShwiK7Ue0YXpyqeo4gQmwU0=',
    'osd': 'V1wUA0rHyV5UZhOtPMKsjboQLVov9Z01IxZ-z0_0nzwHBi_icztBvzRjF6k87ZAHShUvLr0e2Ijswqeh7wEuwUQ=',
    '_zap': 'f6ccf2bc-46aa-4070-8d62-5397f4dfe399',
    'd_c0': 'AABTrrmvNhePTvsuCtZDG3OSlSEm0GffC6Y=|1691586935',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1708596863,1708933559',
    'YD00517437729195%3AWM_NI': 'aNuuRTfGIUfytZxkYzHtNjSyW4mz46GpdeFNYA9qUes5bm%2FzDDIwqtOCkfsaCrA1FNfylwgCfkwsjJi%2FXpsKO164gWRw5PVQgxDngRV0YEI3OgYu3pfUam0AA%2FlUYyjSakE%3D',
    'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6eeafea7486e9feaecb79f7b08eb6d45e878f9f86d1398693bea3e75f819284a3e52af0fea7c3b92aa392bb96d160a69987b6e573b886b88cdc728cac828bd27395eca39bb73e85b0ac86c5469b9ff792d86fb1ebae8eae72889c8798f4808d9da587f26b81ae8fd2c546a6a7a498e649a6b5b994e942abf19891f2418deffad5e65d92a9fbb1d55ba5a88c8fe65a96f097a6cc398db99796b27ca68baf8eb34b83f1a4b6dc73aa8daf8cc837e2a3',
    'YD00517437729195%3AWM_TID': 'M3U2O3JdrqNFAUEARUbVx7OYelB1hVxW',
    'z_c0': '2|1:0|10:1709202105|4:z_c0|80:MS4xazJBdElnQUFBQUFtQUFBQVlBSlZUWDlzeEdaUUtzOEtFVUJrMVVGa0lreW9jV2N4dlV3aDZBPT0=|830b577d6570c680407c4bf9acbffb1174f301afd5778bcf4f16bcd6c5a51452',
    '_xsrf': '21725de9-731d-485d-82fc-715ec8dac90f',
    'KLBRSID': 'c450def82e5863a200934bb67541d696|1709280513|1709280502',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1709280513',
    'tst': 'r',
    'BAIDU_SSP_lcr': 'https://www.baidu.com/link?url=m7Dvl5qAN8-HlsUxn78vW7OllNZcv7-TFWqKQP25S7a&wd=&eqid=cf7341e70008f3c30000000465e18cf1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://www.zhihu.com/',
    'Alt-Used': 'zhuanlan.zhihu.com',
    'Connection': 'keep-alive',
    'Cookie': '__snaker__id=JLQ9VlhGktmaN3Cd; SESSIONID=ByMOaO5jzKuQ8QY94GP7QuIaBtGyDHF6WylAzbEwVp9; JOID=WlkcA0PKzFZUbx6oNMKlgL8YLVMi8JU1Kht7x0_9kjkPBibvdjNBtjlmH6k14JUPShwiK7Ue0YXpyqeo4gQmwU0=; osd=V1wUA0rHyV5UZhOtPMKsjboQLVov9Z01IxZ-z0_0nzwHBi_icztBvzRjF6k87ZAHShUvLr0e2Ijswqeh7wEuwUQ=; _zap=f6ccf2bc-46aa-4070-8d62-5397f4dfe399; d_c0=AABTrrmvNhePTvsuCtZDG3OSlSEm0GffC6Y=|1691586935; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1708596863,1708933559; YD00517437729195%3AWM_NI=aNuuRTfGIUfytZxkYzHtNjSyW4mz46GpdeFNYA9qUes5bm%2FzDDIwqtOCkfsaCrA1FNfylwgCfkwsjJi%2FXpsKO164gWRw5PVQgxDngRV0YEI3OgYu3pfUam0AA%2FlUYyjSakE%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeafea7486e9feaecb79f7b08eb6d45e878f9f86d1398693bea3e75f819284a3e52af0fea7c3b92aa392bb96d160a69987b6e573b886b88cdc728cac828bd27395eca39bb73e85b0ac86c5469b9ff792d86fb1ebae8eae72889c8798f4808d9da587f26b81ae8fd2c546a6a7a498e649a6b5b994e942abf19891f2418deffad5e65d92a9fbb1d55ba5a88c8fe65a96f097a6cc398db99796b27ca68baf8eb34b83f1a4b6dc73aa8daf8cc837e2a3; YD00517437729195%3AWM_TID=M3U2O3JdrqNFAUEARUbVx7OYelB1hVxW; z_c0=2|1:0|10:1709202105|4:z_c0|80:MS4xazJBdElnQUFBQUFtQUFBQVlBSlZUWDlzeEdaUUtzOEtFVUJrMVVGa0lreW9jV2N4dlV3aDZBPT0=|830b577d6570c680407c4bf9acbffb1174f301afd5778bcf4f16bcd6c5a51452; _xsrf=21725de9-731d-485d-82fc-715ec8dac90f; KLBRSID=c450def82e5863a200934bb67541d696|1709280513|1709280502; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1709280513; tst=r; BAIDU_SSP_lcr=https://www.baidu.com/link?url=m7Dvl5qAN8-HlsUxn78vW7OllNZcv7-TFWqKQP25S7a&wd=&eqid=cf7341e70008f3c30000000465e18cf1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    'TE': 'trailers',
}

for i in text_id:
    response = requests.get('https://zhuanlan.zhihu.com/p/' +
                            i, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('title').text

    with open(f"./爬虫/{title}.md", 'w', encoding='utf-8') as f:
        f.write(html_to_md(response.text))
