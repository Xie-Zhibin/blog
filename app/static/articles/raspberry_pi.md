#树莓派初体验

觊觎树莓派已久，记得初次见面是在一个科技展中看到的，卡片大小的芯片被放在一个不起眼的角落，庆幸的是还是让我发现了，后来一次偶然的机会在JD上看到了树莓派的身影，点击查看详情，便决心买下一块用来学习娱乐。

>维基百科：树莓派（英语：Raspberry Pi），是一款基于Linux的单板机电脑。它由英国的树莓派基金会所开发，目的是以低价硬件及自由软件刺激在学校的基本计算机科学教育。树莓派只有一张信用卡大小，体积大概是一个火柴盒大小，可以运行像《雷神之锤III竞技场》的游戏和进行1080p视频的播放。操作系统采用开源的Linux系统如Debian、ArchLinux，自带的Iceweasel、KOffice等软件，能够满足基本的网络浏览、文字处理以及电脑学习的需要。
>树莓派基金会提供了基于ARM架构的Debian、Arch Linux和Fedora等的发行版供大众下载，还计划提供支持Python作为主要编程语言，支持BBC BASIC(通过RISC OS映像或者Linux的"Brandy Basic"克隆)、C语言和Perl等编程语言。


刚拿到树莓派的时候还是被惊喜到了，比想象中的还要小巧。然后给它装上专门给pi的原生系统raspbian，raspbian是一个基于debian的linux操作系统，它也有没有图形化界面的lite版本，如果是把pi用来当做服务器用的话可以考虑不用图形化界面，可以节省很多宝贵的资源。安装系统很简单，pi3的外存是TF卡，只需要把下载的镜像用专门的软件烧录进去就可以了，傻瓜式操作，甚至连分区都不用自己管(这也许是一个弊端)。关于教程可以直接google获取去官网[(https://www.raspberrypi.org)](https://www.raspberrypi.org)找.
树莓派3吸引我的地方除了它可定制性强和性价比高以外，还有一个特别重要的是它的40根GPIO针脚。GPIO是General Purpose Input Output （通用输入/输出）的简称，可以用它做电子设备的控制信号。
一个例子是:由于pi3发热量比较大，光有散热片是不够的，还需要风扇进行冷却，GIOP提供了两个3.3V和两个5V的直流电输出，可以用来给风扇提供电源，然而问题在于，这4个直流输出是不受系统控制的，只要给机器通上电，风扇就会不停地转动，无法关闭，这不符合程序猿的思维。而且GPIO输出也是用来当做电信号的，输出功率低，无法推动大功率的风扇。于是这里就需要一个控制电路来控制风扇自动给机器散热。
可以用继电器或者三极管当做风扇的开关，用gpio信号控制开关的通断。继电器和三极管都可以在某宝上买到，这里用型号为S8550的三极管。

实现功能：让风扇自动散热，cpu超过60度时发送邮件通知.参考:[这篇文章](https://wusiyu.me/%E8%AE%A9%E6%A0%91%E8%8E%93%E6%B4%BE%E6%A0%B9%E6%8D%AE%E6%B8%A9%E5%BA%A6%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E6%95%A3%E7%83%AD%E9%A3%8E%E6%89%87%E7%9A%84%E5%90%AF%E5%81%9C/)
代码:

```
#coding:utf-8
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import RPi.GPIO as GPIO
import time

def adjust_fan():
    """auto adjust fan"""
    pin = 15 # 用第15根gpio针脚输出做控制信号
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    while True:
        try:
            file = open('/sys/class/thermal/thermal_zone0/temp') # 读取CPU温度
            temp = int(file.readline())
        except (IOError,ValueError), e:
            temp = 50000

        if (temp >= 46000):
            GPIO.output(pin, False) # 超过46度，开始散热

        if (temp < 40000):
            GPIO.output(pin, True) # 低于40度，停止散热

        if (temp >= 60000):
            send_email() # 超过60度，给管理员发送紧急通知

        time.sleep(5)

    return 0

def send_email():
    """send information to admin"""
    from_addr = '******' # 发送通知的邮箱
    email_password = '******'  # 密码
    smtp_server = 'smtp.163.com'  # smtp服务器地址
    to_addr = ["*******"]  # 用户的邮箱地址，列表
    header = "CPU too hot"
    text = "Dear master, the CPU of your raspberry pi3 is too hot now!"
    msg = MIMEText(text, 'plain', 'utf-8')  # 构造MIMEText对象
    msg['Subject'] = Header(header, 'utf-8')  # 邮件主题
    msg['From'] = "NCUHome <%s>" % from_addr  # 邮件发送方
    msg["To"] = "You <Your_Email>"  # 邮件接收方

    server = smtplib.SMTP(smtp_server, 25)
    server.starttls()  # 建立安全连接，QQ,Gmail必须加密传输
    server.login(from_addr, email_password)  # 登录smtp服务器
    server.sendmail(from_addr, to_addr, msg.as_string())  # 发送邮件
    server.quit()  # 登出服务器
    return "done"


if __name__ == '__main__':
    adjust_fan()

```
需要注意的是风扇用了两个阀值来控制风扇。如果只用一个临界值的话，会出现这种情况：风扇会有规律地忽停忽转，这样并不能很好地达到散热和省电的效果。

完成以后，可以将这段代码放到一个专门的地方，然后在/etc/rc.local 中添加这个py代码运行的命令脚本，这样它就能开机自启并且实时监控cpu温度了。
现在我的树莓派只插上了电源，里面运行了几个用python写的学校内网爬虫，用来爬取有用的信息。让路由器绑定了网卡的MAC地址，这样至少再内网输煤派是有固定ip的，方便访问，平时用ssh来操作它，已经无压力地运行了一个星期。最主要的问题是稳定可靠的电源，学校经常无故停电，导致树莓派停机。

这个算是我第一次实现了用代码直接控制硬件，挺振奋人心的，但树莓派的可玩性远远不止这点，还有更多好玩的东西等着我们去探究发现！