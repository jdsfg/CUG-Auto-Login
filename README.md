# 🛡️ CUG-Net-Guardian | 地大校园网认证守护脚本

> 彻底告别每天数次登录校园网网页的痛苦！此外本脚本旨在将Ubuntu 服务器打造成一个**永久在线**的私有数据中心。

## 🌟 项目亮点 

* **企业级环境**：模拟生产环境下的自动化登录和保活机制。
* **Systemd 部署**：利用 Linux 系统服务，实现开机自启和断线自动重连。
* **网络编程**：使用 Python `requests` 库实现 HTTP/HTTPS 协议交互，绕过 Portal 网页认证。
* **低资源占用**：静默运行于命令行环境，资源消耗极低。

## ⚙️ 工作原理

本脚本为 CUG 校园网用户提供 Systemd 服务，自动在后台检测网络状态，并在断线后使用 Python 脚本自动完成深澜 (Srun) 认证登录。

## 🚀 部署指南 (Deploy)

### 1. 环境要求

* 操作系统: Ubuntu 20.04+ (服务器/WSL)
* Python: 3.6+
* 依赖: `requests` 库
  
### 2.流程

1.  将 `config.sample.json` 复制为 `config.json`，并填入您的学号、密码和 `ac_id=3`。
2.  安装依赖：`pip3 install requests`
3.  配置 Systemd 服务启动 `main.py`。

---
