import requests
from lxml import etree
import os
import time
import datetime as dt

#data acquire
#data analyse
#data output
#cycle

while True:
    url = "http://law.suda.edu.cn/"
    content = requests.get(url).content
    html = etree.HTML(content)
    title = html.xpath("/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/ul/li[1]/span/a/@title")[0]
    print("当前的标题为:%s" % title)
    if not os.path.isfile("F:\study\Python\craw\\title_temp.txt"):
        # 判断title_temp.txt文件是否存在，不存在则创建，并写入获取的第一篇文章标题
        f = open("D:\study\Python\craw\\title_temp.txt", "w")
        f.write(title)
        print("将当前标题记录在:F:\study\Python\craw\\title_temp.txt中，等待检测")
        f.close()
    else:
        # title_temp.txt文件存在的话，提取里面标题，和获取的标题对比
        with open("F:\study\Python\craw\\title_temp.txt", "r+") as f:
            old_title = f.read()
            if old_title != title:
                # 如果读取内容和获取的网站第一篇文章标题不一致，则表明网站更新
                sckey = 'SCU98402T320035cb43dcf655179392ee923a63bb5ec3a8214b2eb'  # 在发送消息页面可以找到
                url = 'https://sc.ftqq.com/%s.send?text=网站更新了哦(*￣▽￣*)&desp=info1' % sckey  # text为推送的title,desp为推送的描述
                requests.get(url)  # 发送微信推送

                f.seek(0)
                f.truncate()
                print("网站有更新，需通知")
                f.write(title)
                # 写入最新的标题内容，方便下一次比对
                break
                # 退出循环
            else:
                # 否则的话，表明网站没有更新
                now_time = dt.datetime.now().strftime('%F %T')
                print('还木有更新🍻‍(*￣▽￣*)🍻当前时间为：' + now_time)  # 获取当前时间
    time.sleep(5)