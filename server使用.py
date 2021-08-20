import requests

sckey = 'SCU98402T320035cb43dcf655179392ee923a63bb5ec3a8214b2eb'#在发送消息页面可以找到
url = 'https://sc.ftqq.com/%s.send?text=网站更新了哦(*￣▽￣*)&desp=info1'%sckey#text为推送的title,desp为推送的描述
requests.get(url)