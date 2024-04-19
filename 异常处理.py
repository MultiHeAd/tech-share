# 用来解决一些不可预计的错误，比如说网络连接
"""
可以用try和except来写
"""
import requests

while True:
    url = input("请输入网址")

    try:
        res = requests.get(url=url)
    except Exception as e:  # e是error是一个对象.Exception是全部异常
        print("请求失败，原因: {}".format(str(e)))
        continue

    with open('content.txt',mode='w') as f:
        f.write(res.text)
