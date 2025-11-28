import requests
import time
import json
import os

# 加载配置文件
CONFIG_FILE = "config.json"

if not os.path.exists(CONFIG_FILE):
    print(f"❌ 错误：找不到配置文件 {CONFIG_FILE}")
    print("请复制 config.sample.json 为 config.json 并填入你的账号密码。")
    exit(1)

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

USERNAME = config["username"]
PASSWORD = config["password"]
HOST = config["host"]
AC_ID = config["ac_id"]

# ... 下面的代码保持原来的逻辑不变 ...
# ... 为了节省篇幅，这里只要把原来定义的 USERNAME/PASSWORD 变量删掉即可 ...
# ... login() 函数和 check_net() 函数直接使用上面的变量 ...

def login():
    url = f"http://{HOST}/cgi-bin/srun_portal"
    params = {
        'action': 'login',
        'username': USERNAME,  # 这里不用加 DOMAIN 了，或者你在 json 里配
        'password': PASSWORD,
        'ac_id': AC_ID,
        'ip': '',
        'chksum': '',
        'info': '',
        'n': '200',
        'type': '1',
        'os': 'Linux',
        'name': 'Linux',
        'double_stack': '0',
        'ajax': '1'
    }

    print(f"正在尝试登录 IP: {HOST} ...")
    try:
        session = requests.Session()
        session.trust_env = False
        res = session.get(url, params=params, timeout=5)
        if "login_ok" in res.text:
            print(">>> ✅ 登录成功！ <<<")
            return True
        else:
            print(f">>> ❌ 登录失败: {res.text[:50]}...")
            return False
    except Exception as e:
        print(f"连接报错: {e}")
        return False

def check_net():
    try:
        session = requests.Session()
        session.trust_env = False
        session.get("http://www.baidu.com", timeout=3)
        return True
    except:
        return False

if __name__ == "__main__":
    while True:
        if check_net():
            print(f"[{time.strftime('%H:%M:%S')}] 网络正常。")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] 网络断开，执行登录...")
            login()
        time.sleep(300)
