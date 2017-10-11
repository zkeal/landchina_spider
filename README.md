# landchina_spider
基于landchina的爬虫，主要爬取结果公告，市场交易下的选项

landchina 对应结果公告  --》 spider name: DistrictTree
transaction1 对应市场交易\土地转让  --》 spider name: transaction1
transaction2 对应市场交易\土地出租  --》 spider name: transaction2
transaction3 对应市场交易\土地抵押  --》 spider name: transaction3

Windows 下安装
1.安装python
根据你的需求下载python安装包，安装python（本文基于python27）	https://www.python.org/downloads/　　
在 环境变量---"Path"中加入路径："安装目录/python27/;安装目录/python27/Scripts;"
在运行中输入"cmd"打开命令窗口，输入"python --version"，如果成功显示python版本号，则python安装成功！如果未显示，则重启计算机！　　
2.安装pywin32
根据需要下载相应的pywin32安装包
https://sourceforge.net/projects/pywin32/files/pywin32/Build%20217安装lxml
重启cmd命令窗口，输入"pip --version"，若显示pip版本号，则安装成功！
3.安装pyOpenSSL等
重启cmd命令窗口，用pip安装openSSL，输入命令"pip install pyOpenSSL"
以及 
pip install xlwt
pip install requests
4.安装scrapy
准备工作完成，安装scrapy。重启cmd命令窗口，用pip安装openSSL，输入命令"pip install 	scrapy"
等待自动安装，安装完成后输入"scrapy"，提示scrapy的命令提示内容，则整个安装过程结束。
5. 在cmd 中运行scrapy startproject landchina   ,然后将zip文件解压。将landchina 目录覆盖替换

6.在landchina 目录下运行 scrapy crawl DistrictTree ，爬虫开始运行，结果xls in fo.xls  会在该目录下生成。


注意：1.由于需要通过安全狗验证以及网络波动等原因，可能会丢失少量数据
      2.爬去过程中请勿强行关闭，需要关闭时使用一次ctrl + c 等待关闭即可，否则会被当作恶意抢占资源导致ip被封禁（应该会被当作SYN DDOS攻击）。

使用方法：
到scrapy 项目目录下面运行，会自动生成info.xls 的结果文件
scrapy crawl DistrictTree -a date='2017-01-01~2017-02-01' 
就会自动爬取2017-01-01 至2017-02-01 的所有数据

PS:
1.目前设置当线程 ，delay 12S,多了landchina的服务器受不住，也有可能被封禁。
2.使用代理的话请按照 可以参考 https://github.com/kohn/HttpProxyMiddleware  也可以自己实现Middleware
3.landchina 的接口验证固定参数可能会不定期更新，我这边有空会看一下如何优化。
4.目前部署方式路子比较野，找时间完善一下

另外其他问题请联系 zkeal@outlook.com
欢迎大家多多交流

给一个土地抵押的截图
![image](https://github.com/zkeal/landchina_spider/blob/master/example.PNG)
