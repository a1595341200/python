from tokenize import cookie_re
import requests
import json

# kw = {'wd': "京东"}


def myget(url, kw, headers):
    response = requests.get(
        url, params=kw, headers=headers)
    fo = open("foo.html", "w")
    fo.write(response.text)
    fo.close()
    return response


def mypost(url, data, headers):
    response = requests.post(
        url, data=data, headers=headers)
    fo = open("foo.html", "w")
    fo.write(response.text)
    fo.close()
    return response


headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive", "Cookie": "GUID=2417c62408532442; sidyaohuo=07E5226CB5BF4E6_AE5_08644_39540_81001-2-0-0-0-0; __gads=ID=cf2cc34e4f40c1f3-22daac561dd1007d:T=1648083235:RT=1648083235:S=ALNI_Mak9CAZ5aFZzFBYQZ1-7InNudtSYw; ASP.NET_SessionId=ykbn3q45fvgbste1ks1onf55; __gpi=UID=000005db80ade5e4:T=1653665361:RT=1653665361:S=ALNI_MblqyQCtGqaU7SQQdgjnzXM1TM8Iw; GET38645=", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "TE": "trailers"}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
# response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)
response = requests.get(
    "https://yaohuo.me/wapindex.aspx?sid=-2", headers=headers)

# 查看响应内容，response.text 返回的是Unicode格式的数据
# print(response.text)
# kw = {"action": "go", "id": "1059534", 'sitid': "1000",
#       "classid": "177", "lpage": "1"}
# response = requests.get(
#     "https://yaohuo.me/bbs/book_view_mod.aspx", params=kw, headers=headers)
# postkw = {"needpassword": "m321145",
#           "sid": "07E5226CB5BF4E6_AE5_08644_36100_91001-2-0-0-0-0", "go": "确定"}
# response = requests.post(
#     "https://yaohuo.me/bbs/book_view_mod.aspx", data=postkw, headers=headers)
headers = {
    "Host": "yaohuo.me",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie": "GUID=2417c62408532442; sidyaohuo=07E5226CB5BF4E6_AE5_08644_36100_91001-2-0-0-0-0; __gads=ID=cf2cc34e4f40c1f3-22daac561dd1007d:T=1648083235:RT=1648083235:S=ALNI_Mak9CAZ5aFZzFBYQZ1-7InNudtSYw; __gpi=UID=000005db80ade5e4:T=1653665361:RT=1655646701:S=ALNI_MblqyQCtGqaU7SQQdgjnzXM1TM8Iw; ASP.NET_SessionId=kd2jul45ibhqzyzy0mwwwy2t",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}

response = requests.get("https://yaohuo.me/bbs-1075802.html", headers=headers)

headers = {
    "Host": "yaohuo.me",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie": "GUID=2417c62408532442; sidyaohuo=07E5226CB5BF4E6_AE5_08644_36100_91001-2-0-0-0-0; __gads=ID=cf2cc34e4f40c1f3-22daac561dd1007d:T=1648083235:RT=1648083235:S=ALNI_Mak9CAZ5aFZzFBYQZ1-7InNudtSYw; __gpi=UID=000005db80ade5e4:T=1653665361:RT=1655646701:S=ALNI_MblqyQCtGqaU7SQQdgjnzXM1TM8Iw; ASP.NET_SessionId=kd2jul45ibhqzyzy0mwwwy2t",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}
kw = {"siteid": 1000, "classid": 177, "id": 1075802, "lpage": 1}
myget("https://yaohuo.me/bbs/Book_View_admin.aspx", kw, headers)
headers = {
    "Host": "yaohuo.me",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie": "GUID=2417c62408532442; sidyaohuo=07E5226CB5BF4E6_AE5_08644_36100_91001-2-0-0-0-0; __gads=ID=cf2cc34e4f40c1f3-22daac561dd1007d:T=1648083235:RT=1648083235:S=ALNI_Mak9CAZ5aFZzFBYQZ1-7InNudtSYw; __gpi=UID=000005db80ade5e4:T=1653665361:RT=1655646701:S=ALNI_MblqyQCtGqaU7SQQdgjnzXM1TM8Iw; ASP.NET_SessionId=kd2jul45ibhqzyzy0mwwwy2t",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}
kw = {"action": "go", "id": 1075802, "siteid": 1000, "classid": 177, "lpage": 1}
response = myget("https://yaohuo.me/bbs/book_view_mod.aspx", kw, headers)
headers = {
    "Host": "yaohuo.me",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "94",
    "Origin": "null",
    "Connection": "keep-alive",
    "Cookie": "GUID=2417c62408532442; sidyaohuo=07E5226CB5BF4E6_AE5_08644_36100_91001-2-0-0-0-0; __gads=ID=cf2cc34e4f40c1f3-22daac561dd1007d:T=1648083235:RT=1648083235:S=ALNI_Mak9CAZ5aFZzFBYQZ1-7InNudtSYw; __gpi=UID=000005db80ade5e4:T=1653665361:RT=1655646701:S=ALNI_MblqyQCtGqaU7SQQdgjnzXM1TM8Iw; ASP.NET_SessionId=kd2jul45ibhqzyzy0mwwwy2t",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
}
data = {"needpassword": "m321145",
        "sid": "07E5226CB5BF4E6_AE5_08644_36100_91001-2-0-0-0-0", "go": "%E7%A1%AE%E5%AE%9A"}
response = mypost(
    "https://yaohuo.me/404.htm?aspxerrorpath=/bbs/book_view_mod.aspx", data, headers)

# 查看响应内容，response.content返回的字节流数据
print(response.content)

# 查看完整url地址
print(response.url)

# 查看响应头部字符编码
print(response.encoding)

# 查看响应码
print(response.status_code)

print(response.text)
