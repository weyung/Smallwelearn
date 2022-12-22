# WELearn 填空助手

## 声明

* 代码采用 MIT 协议开源，欢迎 Fork 和 Star。
* 本脚本仅供学习交流使用，对于使用本脚本造成的任何后果，均由使用者本人承担。

## 介绍

WelearnHelper 的简化版本，写的时候主要是现有的 WelearnHelper 不能自动填填空题，所以就自己写了一个，采用的是 pyppeteer 库，所以需要 Chrome 浏览器。
由于个人英语课上做的是视听说教程，故只对视听说做了支持，其他课程可能需要自己修改代码。
同时脚本只能自动填空题，其他题目建议先用 WelearnHelper 做完。

## 使用

### 安装

确保有 Python 环境和 Chrome 浏览器。
下载源代码，缺少的库自行 pip 安装。

### 配置

在 `settings_template.json` 中填写你的 Welearn 账号和密码，然后将文件名改为 `settings.json`。

### 运行

运行 `main.py`，程序会自动打开 Chrome 浏览器，然后自动完成。

### 其他

目前只能全自动，就是从头做到尾，不支持从中间开始，但是总共也就几分钟的事。
