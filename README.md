# WELearn 填空助手

## 声明

* 代码采用 MIT 协议开源，欢迎 Fork 和 Star。
* 本脚本仅供学习交流使用，对于使用本脚本造成的任何后果，均由使用者本人承担。

## 介绍

本脚本为 WelearnHelper 的简化版本，功能有限：

* 仅支持**视听说**，其它课程可根据需要自行更改代码。
* 仅自动完成**填空题**，需要手动点击提交。

答案来源于 Welearn 官网（连着题目一起发过来的），正确性基本可以保证。

## 使用

### 安装

确保已安装 Python 环境和 Chrome 浏览器。
下载源代码，缺少的库请自行 pip 安装。

### 配置

在 `settings_template.json` 中修改以下项，然后将文件名改为 `settings.json`。

* `chrome_path`：Chrome 浏览器的路径
* `username`：Welearn 帐号
* `password`：密码
* `course`：视听说版本，默认为 `3`

### 运行

运行 `main.py`，程序会自动打开 Chrome 浏览器并从头开始完成题目。
注意浏览器**不能在后台运行**，否则程序会暂停。
每完成一次填空程序会暂停供用户选择提交与否，然后可以切换到终端输入 `Enter` 继续（注意此时需要切回浏览器）。

### 其他

写这个脚本的起因是现有的 Welearn 脚本不能自动完成填空题，有些人可以接受自己照着答案再填一遍，但偏偏本人就是懒到这点力气都不肯花（）
基于不重复造轮子的原则，我没有对除填空题以外的题型做支持，如果有需要的话可以自行添加，应该也是不难的。但本人还是建议先用 WelearnHelper 把能做的做了，再用这个脚本做填空题。

### 吐槽

开发中最大的困难之一就是对官网的答案做解析，其中竟然还有错误的单词。。。
