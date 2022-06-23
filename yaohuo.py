from email import header
import requests


def log(response):
    fo = open("foo.html", "w")
    fo.write(response.text)
    fo.close()


cookie = {
    "GUID": "2417c62408532442",
    "sidyaohuo": "07E5226CB5BF4E6_AE5_08647_34410_81001-2-0-0-0-0",
    "__gads": "ID=cf2cc34e4f40c1f3-22daac561dd1007d:T=1648083235:RT=1648083235:S=ALNI_Mak9CAZ5aFZzFBYQZ1-7InNudtSYw",
    "__gpi": "UID=000005db80ade5e4:T=1653665361:RT=1655646701:S=ALNI_MblqyQCtGqaU7SQQdgjnzXM1TM8Iw",
    "ASP.NET_SessionId": "kd2jul45ibhqzyzy0mwwwy2t",
    "GET38645": "0B7B8868D17BABE8"
}


def login():
    # login_url可以通过抓包工具获取，也可以通过表单的action=""获取
    # https://17865918382:m321145@yaohuo.me/blog/login.html/waplogin.aspx
    login_url = "https://yaohuo.me/waplogin.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"
    }
    body = {
        "logname": "17865918382",
        "logpass": "m321145",
        "action": "login",
        "classid": 0,
        "siteid": "1000",
        "sid": "backurl=wapindex.aspx%3Fsid%3D-2",
        "referer": ""
    }
    try:
        res = requests.post(url=login_url, headers=headers, data=body)
        mid_cookies = res.cookies
        # 把返回的cookie转换为字典
        cookie = requests.utils.dict_from_cookiejar(mid_cookies)
        log(res)
        print(cookie)
        return cookie
    except Exception as err:
        print('获取cookie失败: \n{0}'.format(err))


def modText(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
        "Connection": "keep-alive"
    }
    body = {"needpassword": "m321145",
            "sid": cookie['sidyaohuo'],
            "go": "%E7%A1%AE%E5%AE%9A"}
    try:
        res = requests.post(url=url, headers=headers,
                            data=body, cookies=cookie)
        log(res)
        return cookie
    except Exception as err:
        print('修改帖子失败: \n{0}'.format(err))


def myget(url, kw):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"
    }

    try:
        res = requests.get(url=url, headers=headers, params=kw, cookies=cookie)
        log(res)
    except Exception as err:
        print('get失败: \n{0}'.format(err))


def mypost(url, kw):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
        "Connection": "keep-alive"
    }
    try:
        res = requests.post(url=url, headers=headers,
                            data=kw, cookies=cookie)
        log(res)
        print(res.status_code)
        return cookie
    except Exception as err:
        print('修改帖子失败: \n{0}'.format(err))


def edit_post_content():
    # 修改帖子内容
    kw = {"face": "",
          "stype": "",
          "book_title": "京东家宽车",
          "book_content": "[url=http://jdgjzi.natappfree.cc]一键上车[/url]\n稳定不宕机 5车请自行选择车号上车",
          "action": "gomod",
          "id": 1075802,
          "classid": 177,
          "siteid": 1000,
          "lpage": 1,
          "sid": "07E5226CB5BF4E6_AE5_08647_34410_81001-2-0-0-0-0",
          "bt": "%E4%BF%AE+%E6%94%B9"
          }
    mypost("https://yaohuo.me/bbs/book_view_mod.aspx", kw)


if __name__ == '__main__':
    # edit_post_content()
    login()
