from flask import Flask, request, redirect
import random
import string
import json

app = Flask(__name__)

# 生成短链接的函数


def abc():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))

# 读取


def abc_1():
    try:
        with open('urls.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# 导入进urls.json


def abc_2(abc_3):
    with open('urls.json', 'w') as f:
        json.dump(abc_3, f)


@app.route('/')
def home():
    abc_4 = request.args.get("web")
    if abc_4 is None:
        return "no bro 用法: exp.com/?web=http://xxx"
    # 生成一个短链接
    abc_5 = abc()
    abc_6 = abc_1()
    abc_6[abc_5] = abc_4
    abc_2(abc_6)
    return request.host_url + abc_5


@app.route('/<abc_5>')
def redirect_to_url(abc_5):
    # 保存长链接和短链接
    abc_6 = abc_1()
    abc_7 = abc_6.get(abc_5)
    if abc_7 is None:
        return "no bro 不存在"
    # 将用户重定向到长链接
    return redirect(abc_7)


# 开端口用于访问
if __name__ == '__main__':
    app.run(port=5000)
