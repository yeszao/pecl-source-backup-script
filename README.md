# PECL 和 PHP 源码包下载脚本

### 1. 使用方法
1. clone 本仓库。
2. 创建虚拟环境并安装依赖：
    ```bash
    sudo apt-get install python-pip3
    pip3 install virtualenv
    virtualenv venv --python=python3
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. 采集：
    ```bash
    scrapy crawl pecl  # 下载 pecl 源码包
    scrapy crawl php   # 下载 php 源码包
    ``` 
    下载的源码包在 `downloads` 目录下。
    
### 2. 定时执行
```bash
30 2 * * * cd <project_dir> && source venv/bin/activate && scrapy crawl pecl
30 3 * * * cd <project_dir>/downloads/pecl && git add . && git commit "update" && git push github master && git push gitee master 

```