# 🛡️ CUG-Net-Guardian | 地大校园网认证守护脚本

> 彻底告别每天数次登录校园网网页的痛苦！此外本脚本旨在将Ubuntu 服务器打造成一个**永久在线**的私有数据中心。

## 🌟 项目亮点 

* **企业级环境**：模拟生产环境下的自动化登录和保活机制。
* **Systemd 部署**：利用 Linux 系统服务，实现开机自启和断线自动重连。
* **网络编程**：使用 Python `requests` 库实现 HTTP/HTTPS 协议交互，绕过 Portal 网页认证。
* **低资源占用**：静默运行于命令行环境，资源消耗极低。

## ⚙️ 工作原理

本脚本利用您路由器搭建的稳定内网 (WISP 模式)，每隔 5 分钟检测一次百度连通性。一旦发现网络断开，则立即向认证服务器 (192.168.167.115) 发送带学号密码的登录请求，确保网络不中断。

## 🚀 部署指南 (Deploy)

### 1. 环境要求

* 操作系统: Ubuntu 20.04+ (服务器/WSL)
* Python: 3.6+
* 依赖: `requests` 库

### 2. 配置账号

请将 `config.sample.json` 文件复制为 `config.json`，并填入你的真实信息。

```bash
cp config.sample.json config.json
nano config.json
