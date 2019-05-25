#autoTestGo简介


###这是一个接口自动化测试框架，整套框架由requests + unittest + ddt +pymysql + BeautifulReport模块组成， 测试用例在yaml文件#中，支持数据驱动、连数据库查询。 目前框架还不是特别完善，需要在后续的使用中一步步优化，目前尚未使用jenkins做集成，后续结合jenkins做成持续集成

##环境配置
###1、requests  
###2、ddt  
###3、pymysql  
###4、BeautifulReport

##注意事项
###需要把BeautifulReport文件夹放到python的lib文件site-packages下面  
![Alt text](https://github.com/shaoyan163/autoTestGo/blob/master/screenshot/lib.png)

##实现的功能
###1、数据驱动  
###2、接口依赖  
###3、连接数据库查询  
###4、自动生成测试报告  
###5、自动发送测试邮件

#模块介绍
![Alt text](https://github.com/shaoyan163/autoTestGo/blob/master/screenshot/module.jpg)  
###1、common 中主要放公共方法，操作数据库、读取配置文件、写token、发送邮件等 
###2、conf主要放配置文件、测试环境地址、数据库地址等在配置文件中 
![Alt text](https://github.com/shaoyan163/autoTestGo/blob/master/screenshot/conf.jpg)
###3 、testCase放每个接口的测试脚本，脚本以test开头
###4、testReport放测试报告
###5、yaml内放的是每个接口测试用例
![Alt text](https://github.com/shaoyan163/autoTestGo/blob/master/screenshot/yaml.jpg)

#测试报告

![Alt text](https://github.com/shaoyan163/autoTestGo/blob/master/screenshot/report.jpg)

###点击查看，可以查看具体报错信息，方便定位问题  

![Alt text](https://github.com/shaoyan163/autoTestGo/blob/master/screenshot/report1.jpg)  
###欢迎使用，使用中有问题欢迎沟通交流，QQ群790710729、个人QQ757899689



