# 1 常用概念

*   时延是一个链路层概念,指的是一个分组在链路中传输所需的时间.
    *   处理时延: 用于检查分组的头部信息决定将这个分组**转发到何处**所耗费的时间.
    *   排队时延: 分组在链路上**等待传输**的时间
    *   传输时延、存储转发时延: 分组长度/链路速率,表示将分组**推送到链路上**所需要的时延.
    *   传播时延:两个路由器之间的数据传输的耗时,距离/传播速度.
*   流量强度: 分组到达队列的平均速度\*分组长度/传播速度,**设计系统时流量强度不应该超过1**
*   丢包: 在实际应用中,流量强度大于1也不会导致排队时延增加,因为路由器的设计是由成本决定的,路由器存储空间占满以后会发送丢包.
*   瞬时吞吐量: 主机接受该文件的速率.吞吐量不仅取决于链路的传输速率,也取决于干扰流量.
*   协议栈:各层所有协议的集合.
- MAC地址: 数据链路层,长度为6字节(48位),用于唯一标识网络适配器(网卡).MAC地址是一个**局域网有效**的地址.因此MAC地址只要经过网关等就会发生改变,因为已经换了局域网.

- 三种计算机网络体系结构
    - ![三种计算机网络体系结构](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E4%B8%89%E7%A7%8D%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84.png)
- TCP/IP体系结构
    - ![TCP/IP体系结构](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/TCP_IP%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84.png)
- **实体**: 是指任何可发送或者接收信息的**硬件**或**软件进程**.
    - **对等实体**: 是指通信双方**相同层次中的实体**
    - ![对等实体](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E5%AF%B9%E7%AD%89%E5%AE%9E%E4%BD%93.png)

- **协议**: 协议是控制两个对等实体在**水平方向**进行**逻辑通信**的规则的集合
    - ![协议](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E5%8D%8F%E8%AE%AE.png)
    *   网络协议三要素:
    *   **语法(Syntax)**:定义所交换信息的**格式**,还决定了数据呈现给接收者的顺序
    *   **语义(Semantics)**:定义通信双方所要完成的**操作**
    *   **同步/时序(Timing)**: 定义通信双方的**时序关系**
        1.  什么时候发送数据？
        2.  发送和接收数据的速度是多少？
            它对数据项进行速度匹配、排序和流量控制。
            示例：发送方可以以 100 Mbps 的速度发送数据，但接收方只能以 20 Mbps 的速度使用数据，则可能会丢失数据或丢包。因此，发送方和接收方之间必须存在适当的同步。
- **服务**: 在协议的控制下，**两个对等实体在水平方向的逻辑通信使得本层能够向上一层提供服务**。
    - 要实现本层协议，还需要使用下面一层所提供的服务。
    - 协议是**水平**的，而服务是**垂直**的。
    - 实体看得见下层提供的服务，但并不知道实现该服务的具体协议。下层的协议对上层的实体是**透明**的。
    - ![服务](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E6%9C%8D%E5%8A%A1.png)
    - 上层要使用下层所提供的服务，必须通过与下层**交换一些命令**，这些命令称为**服务原语**。
    - 对等层次之间传送的数据包称为该层的**协议数据单元**（Protocol Data Unit，PDU）。
    - 同一系统内层与层之间交换的数据包称为**服务数据单元**（Service Data Unit，SDU）。
    - ![PDU和SDU](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/pdu%E5%92%8Csdu.png)
*   DHCP运行机制: Client使用0.0.0.0向255.255.255.255发送**UDP**请求(原先是**BOOTP**请求,UDP是更高级的封装),当DHCP服务器捕获到请求之后**回复ACK**表示成功接收请求.
*   PXE协议解析过程: 服务器启动的时候BIOS或者UEFI加载烧写在网卡ROM中的PXE程序,然后去DHCP服务器请求一个**IP地址和一个pxelinux.0文件**以及PXE服务器IP地址.然后PXE客户端**使用TFTP协议下载pxelinux.cfg文件**,该文件指示了Linux内核和initramfs的位置,接下来便会**加载initramfs**,当Linux内核启动后就可以**根据ks文件实现自动化部署**操作系统.
*   广播风暴: ARP广播的时候会将一个端口收到的数据包转发到其它所有端口,当交换机互联**出现环路**以后,就会形成广播风暴,导致循环发送数据包,硬件资源耗尽.
*   Hub只有一个广播域和冲突域,Switch由一个广播域和多个冲突域,每一个端口在划分VLAN的情况下都是一个冲突域.

## 1.2 广播信道和点对点信道

## 1.2.1 广播信道

# 1.3 NAT

*   NAT的三种模式:
    *   SNAT(源网络地址转换): 是指在数据包从网卡发出去的数据的时候,把数据包中的**源地址部分替换为指定的IP地址**,这样对方就认为数据包的来源是被替换的那个IP的主机.
    *   DNAT: 是指数据包从网卡发送出去的时候,**修改数据包中的目的IP**,表现为如果你想访问A,可是因为网关NAT做了DNAT,把所有访问A的数据包更换为B的IP.
    *   MASQUERADE: 是**用发送数据的网卡上的IP地址替换源IP**,因此对于那些IP不固定的场合,比如**拨号网络**或者通过**DHCP**分配的情况下就可以使用该方式
*   NAT三种模式的区别: 路由是按照目的IP来选择的,因此DNAT是在**pre-routing**链上进行的,而SNAT是数据包发送出去的时候才进行的,因此是**post-routing**链上进行的.
*   转发网关与NAT网关的区别: 两者主要的区别在于**IP地址是否改变.不改变IP地址的网关**,我们称为**转发网关**;**改变IP地址的网关**,我们称为**NAT网关**.

# 2 应用层

## 2.1 FTP协议

FTP文件传输分为两种模式，主动(PORT)模式和被动(Passive)模式
FTP的主要功能是减少或消除在不同操作系统下处理文件的不兼容性.
FTP是**基于TCP**的,FTP使用20端口作为**数据端口**,使用21端口作为**命令端口**,因此控制信息是**带外的**.

*   **主动模式(PORT)**: FTP客户端随机打开一个大于1024的端口N,向服务器21端口发送连接请求,发送FTP用户名和密码,然后打开N+1端口监听,并向服务器发送PORT N+1命令,服务器接收到指令后会使用数据端20连接客户端的N+1端口进行数据传输.
    ![image](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/ftp%E4%B8%BB%E5%8A%A8%E6%A8%A1%E5%BC%8F.png)

*   **被动模式(PASV)**: FTP客户端打开两个任意的本地端口N(大于1024)和N+1.第一个端口连接服务器的21端口,提交PASV命令.然后,服务器会开启一个任意的端口P(大于1024),返回`227 entering passive mode`消息,里面有FTP服务器开放的用来进行数据传输的端口.客户端收到消息取得端口号之后,会通过N+1端口连接服务器的端口P,然后再两个端口之间进行数据传输.
    ![image](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/ftp%E8%A2%AB%E5%8A%A8%E6%A8%A1%E5%BC%8F.png)

### 2.1.2 安全性不佳

FTP传输默认是明文传输，包括客户端发送给服务器用于鉴权的用户名和密码的传输。
虽然新的FTP协议扩展了安全能力，有了FTPS这个基于SSL/TLS协议的新能力，但是新用户要在半天的时间内完成FTP和OpenSSL的配置，是不可能完成的任务，很多系统因此暴露在安全风险中。

## 2.2 DNS协议

### 2.2.1 传统DNS

*   DNS协议使用**53端口,基于UDP协议**,MX记录允许企业将自己的域名作为邮件服务器域名.
*   DNS记录: 由Name,Value,Type,TTL构成的**四元组**.
    *   **A记录**,type=A,name=主机名,value=主机IP
    *   **NS记录**,type=NS,name=主机域,value=权威DNS地址
    *   **CNAME记录**,type=CNAME,name=别名,value=主机名
    *   **MX记录**,type=MX,name=邮件服务地址,value=Web服务地址
    *   **SOA记录**,NS记录和SOA记录是任何一个DNS区域都不可或缺的两条记录,NS记录也叫名称服务记录,用于说明这个区域有哪些DNS服务器负责解析,SOA记录说明负责解析的DNS服务器中哪一个是主服务器.因此,任何一个DNS区域都不可能缺少这两条记录.**NS记录说明了在这个区域里有多少个服务器来承担解析的任务.SOA叫起始授权机构记录,SOA记录说明了在众多NS记录里哪一台才是主要的服务器**.
    *   **SRV记录**,SRV记录是服务器资源记录的缩写.
    *   **PTR记录**,指针记录,PTR记录是A记录的逆向记录,作用是把IP地址解析为域名.
*   传统的DNS存在的问题
    *   **域名缓存**: 运营商缓存和本地缓存
    *   **域名转发**: 某些运营商偷懒将DNS转发到其他运营商,其他运行商返回的是自己网络内部的IP,导致网速慢
    *   出口NAT: 会使得运营商误判
    *   域名更新: 权威DNS更新后其他DNS**更新漫长** (虎牙在全球DNS秒级生效上的实践)

> 域名则由ICANN进行管理。

- **域名组成**
    - ![域名组成](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E5%9F%9F%E5%90%8D%E7%BB%84%E6%88%90.png)

- **顶级域名和二级域名**
    - ![顶级域名和二级域名](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E9%A1%B6%E7%BA%A7%E5%9F%9F%E5%90%8D%E5%92%8C%E4%BA%8C%E7%BA%A7%E5%9F%9F%E5%90%8D.png)
- **域名空间**
    - ![域名空间](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E5%9F%9F%E5%90%8D%E7%A9%BA%E9%97%B4.png)
- **域名服务器类型**
    - ![域名服务器类型](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E5%9F%9F%E5%90%8D%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%B1%BB%E5%9E%8B.png)
    - ![image](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E5%9F%9F%E5%90%8D%E6%9C%8D%E5%8A%A1%E5%99%A8.jpg)
- **dns解析过程**
    - ![dns解析过程](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/dns%E8%A7%A3%E6%9E%90%E8%BF%87%E7%A8%8B.png)
    - ![image](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/dns%E8%A7%A3%E6%9E%90%E6%B5%81%E7%A8%8B.jpg)
- **DNS总结**
    - ![DNS总结](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/DNS%E6%80%BB%E7%BB%93.png)













### 2.2.2 HTTP DNS

*   不走传统的DNS解析,而是自己搭建基于HTTP协议的DNS服务器集群,分布在多个地点和多个运营商.当客户端需要DNS解析的时候,**直接通过HTTP协议**进行请求这个服务器集群,**得到就近的地址**.使用HTTP DNS的,往往是手机应用,需要在手机端嵌入支持HTTP DNS的**客户端SDK**.

## 2.3 HTTP,HTTPS,QUIC协议

### 2.3.1 HTTP与邮箱协议

*   SMTP(Simple Mail Transfer Protocol)管‘发’，POP3(Post Office Protocol)/IMAP(Internet Message Access Protocol)管‘收’。
*   **SMTP**客户端运行在**25端口**,建立与SMTP服务端的连接.
*   HTTP是拉协议,也是非持久连接,**SMTP是推协议,是持久连接**.SMTP要求报文的格式都使用7位ACSII码.发送邮件是推送,接收邮件是拉取,可以借助IMAP(端口:143),POP3(端口:110),HTTP(端口:80)完成.
*   **SMTP**只能发送ASCII码,而互联网邮件扩充MIME可以发送二进制文件.MIME并没有改动或者取代SMTP,而是增加邮件主体的结构,定义了非ASCII码的编码规则.
*   **POP3**的特点是1.POP3允许用户从服务器上把邮件存储到本地主机（即自己的计算机）上,同时删除保存在邮件服务器上的邮件.最新版本的POP3可以不删除邮件.2.客户端的操作（如移动邮件、标记已读等），不会反馈到服务器上
*   **IMAP**协议中客户端和服务器上的邮件保持同步,您在电子邮件客户端收取的邮件仍然保留在服务器上，同时在客户端上的操作都会反馈到服务器上，如：删除邮件，标记已读等，服务器上的邮件也会做相应的动作。

### 2.3.2 HTTP状态码
- 1xx 信息
    - **100 Continue**: 表明到目前为止都很**正常**,客户端可以继续发送请求或者忽略这个响应.
- 2xx 成功
    - 200 OK
    - 204 NO Content: 服务器成功处理了请求，没有返回任何内容.
    - 206 Partial Content: 服务器已经成功处理了部分GET请求。类似于FlashGet或者迅雷这类的HTTP下载工具都是使用此类响应实现断点续传或者将一个大文档分解为多个下载段同时下载。
- 3xx 重定向
    - **301 Moved Permanently: 请求的资源已永久移动到新位置,永久重定向**
    - **302 Found: 临时性重定向**
    - 303 See Other: 和 302 有着相同的功能, 但是 **303明确要求客户端应该采用GET方法获取资源.** 注:虽然HTTP协议规定301,302状态下重定向时不允许把POST方法改成GET方法,但是**大多数浏览器都会在301,302和303状态下的重定向把POST方法改成GET方法**
    - 304 Not Modified: 表示资源在由请求头中的If-Modified-Since或If-None-Match参数指定的这一版本之后，未曾被修改。在这种情况下，由于客户端仍然具有以前下载的副本，因此不需要重新传输资源。
    - 307 Temporary Redirect: 临时重定向,与302的含义类似,但是307要求浏览器**不会把重定向请求的POST方法改成GET方法**
- 4xx 客户端错误
    - 400 Bad Request: 请求报文中存在**语法错误**
    - 401 Unauthorized: 该状态码表示发送的请求**需要有认证信息(BASIC认证, DIGEST认证).**
    - 403 Forbidden: 服务器已经理解请求,但是拒绝执行它,请求被拒绝
    - 404 Not Found
- 5xx 服务端错误
    - 500 Internal Server Error: 服务器正在执行请求时发生错误
    - 502 Bad Gateway: 作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
    - 503 Service Unavailable: 服务器暂时处于**超负载**或者正在进行**停机维护**,现在无法处理请求.

### 2.3.2 HTTP1.1和2.0的区别
- HTTP的报文大概分为三部分.第一部分是**请求行(方法+URL)**

# 运输层
如何**为运行在不同主机上的应用程序提供直接的逻辑通信服务**,就是**运输层的主要任务**.运输层协议又称为端到端协议.

![因特网中的一些典型应用所使用的TCP_IP应用层协议和相应的运输层协议](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E5%9B%A0%E7%89%B9%E7%BD%91%E4%B8%AD%E7%9A%84%E4%B8%80%E4%BA%9B%E5%85%B8%E5%9E%8B%E5%BA%94%E7%94%A8%E6%89%80%E4%BD%BF%E7%94%A8%E7%9A%84TCP_IP%E5%BA%94%E7%94%A8%E5%B1%82%E5%8D%8F%E8%AE%AE%E5%92%8C%E7%9B%B8%E5%BA%94%E7%9A%84%E8%BF%90%E8%BE%93%E5%B1%82%E5%8D%8F%E8%AE%AE.png)

## TCP_IP运输层中的两个重要协议
![TCP_IP运输层中的两个重要协议](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/TCP_IP%E8%BF%90%E8%BE%93%E5%B1%82%E4%B8%AD%E7%9A%84%E4%B8%A4%E4%B8%AA%E9%87%8D%E8%A6%81%E5%8D%8F%E8%AE%AE.png)

## 运输层端口号
![运输层端口号](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E8%BF%90%E8%BE%93%E5%B1%82%E7%AB%AF%E5%8F%A3%E5%8F%B7.png)

## 发送方的复用和接收方的分用
![发送方的复用和接收方的分用](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E5%8F%91%E9%80%81%E6%96%B9%E7%9A%84%E5%A4%8D%E7%94%A8%E5%92%8C%E6%8E%A5%E6%94%B6%E6%96%B9%E7%9A%84%E5%88%86%E7%94%A8.png)

## TCP和UDP的区别

| 传输控制协议TCP | 用户数据报协议UDP |
| --- | --- |
| 面向连接 | 无连接 |
| 每一条TCP连接只能有两个端点EP,只能是一对一通信 | 支持一对一,一对多,多对一和多对多交互通信 |
| 面向字节流 | 面向应用报文 |
| 可靠传输,使用流量控制和拥塞控制 | 尽最大努力交付,即不可靠;不使用流量控制和拥塞控制 |
| 首部最小20字节,最大60字节 | 首部开销小,仅8字节 |

## TCP和UDP的对比
![TCP_UDP对比1](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/TCP_UDP%E5%AF%B9%E6%AF%941.png)

## UDP和TCP对应用层报文的处理
![UDP和TCP对应用层报文的处理](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/UDP%E5%92%8CTCP%E5%AF%B9%E5%BA%94%E7%94%A8%E5%B1%82%E6%8A%A5%E6%96%87%E7%9A%84%E5%A4%84%E7%90%86.png)

## UDP首部和TCP首部的对比
![UDP首部和TCP首部的对比](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/UDP%E9%A6%96%E9%83%A8%E5%92%8CTCP%E9%A6%96%E9%83%A8%E7%9A%84%E5%AF%B9%E6%AF%94.png)

## UDP和TCP对数据传输可靠性的支持情况
![UDP和TCP对数据传输可靠性的支持情况](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/UDP%E5%92%8CTCP%E5%AF%B9%E6%95%B0%E6%8D%AE%E4%BC%A0%E8%BE%93%E5%8F%AF%E9%9D%A0%E6%80%A7%E7%9A%84%E6%94%AF%E6%8C%81%E6%83%85%E5%86%B5.png)

## TCP报文段的首部格式
![TCP报文段的首部格式](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/TCP%E6%8A%A5%E6%96%87%E6%AE%B5%E7%9A%84%E9%A6%96%E9%83%A8%E6%A0%BC%E5%BC%8F.png)

## TCP报文段首部的窗口
![TCP报文段首部的窗口](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/TCP%E6%8A%A5%E6%96%87%E6%AE%B5%E9%A6%96%E9%83%A8%E7%9A%84%E7%AA%97%E5%8F%A3.png)

## tcp首部校验和
![tcp首部校验和](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/tcp%E9%A6%96%E9%83%A8%E6%A0%A1%E9%AA%8C%E5%92%8C.png)

## 三报文握手,建立TCP连接
- **TCP是面向连接的**协议,它基于运输连接来传送TCP报文段
    - TCP运输连接的建立和释放,是**每一次面向连接的通信中必不可少的过程**
- TCP运输连接有以下三个阶段:
    - 通过`三报文握手`来建立TCP连接
    - 基于已建立的TCP连接进行可靠的数据传输
    - 在数据传输结束后,还要通过**四报文挥手**来释放TCP连接
    - ![三报文握手建立TCP连接](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E4%B8%89%E6%8A%A5%E6%96%87%E6%8F%A1%E6%89%8B%E5%BB%BA%E7%AB%8BTCP%E8%BF%9E%E6%8E%A5.png)

- `三报文握手`**建立TCP连接的目的**在于解决以下三个主要问题:
    - 使TCP双方能够**确知对方的存在**
    - 使TCP双方能够**协商一些参数**(例如最大报文段长度,最大窗口大小,时间戳选项等)
    - 使TCP双方能够**对运输实体资源进行分配和初始化**.运输实体资源包括缓存大小,各种状态变量,连接表中的项目等

## TCP三次握手过程

![TCP三次握手过程](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/TCP%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%E8%BF%87%E7%A8%8B.png)
- 客户端发送**TCP连接请求报文段**进入**同步已发送状态**
- **TCP连接请求报文段**和**TCP连接请求确认报文段**首部中的**同步标志位SYN**的值必须设置为1,表明这是一个TCP连接请求报文段,序号seq字段被设置了一个初始值x,作为TCP客户进程所选择的初始序号.
    - TCP规定**同步标志位SYN**被设置位1的报文段(例如TCP连接请求报文段和TCP连接请求确认报文段)不能携带数据,但是要消耗掉一个序号.
    - 按照上述规定,TCP连接请求报文段不能携带数据(即没有数据载荷),但是会消耗掉序号x.
    - 因此,TCP客户进程下一次发送的TCP报文段的数据载荷的第一个字节的序号为x+1
- TCP服务器进程收到TCP连接请求报文段后,如果同意建立连接,则向TCP客户进程发送**TCP连接请求确认报文段**,并进入**同步已接收状态**
    - TCP连接请求确认报文段首部中的**同步标志位SYN和确认标志位ACK的值都设置为1**,表明这是一个**TCP连接请求确认报文段**.
    - 序号seq字段被设置了一个初始值y,作为TCP服务器进程所选择的初始序号.
    - TCP规定**同步标志位SYN**被设置为1的报文段(例如TCP连接请求报文段和TCP连接请求确认报文段)不能携带数据,但是要消耗掉一个序号.
    - **确认号ack**字段的值被设置为x+1,这是对TCP客户进程所选择的**初始号x**的确认
- TCP客户进程收到TCP**连接请求确认报文段**后,还要向TCP服务进程发送针对TCP连接请求确认报文段的**普通TCP确认报文段,并进入连接已建立状态.**
    - 该报文段首部中的**确认标志位ACK**的值被设置为1,表明这是一个普通的TCP确认报文段.
    - 序号seq字段被设置为x+1,这是因为TCP客户进程之前发送的TCP连接请求报文段的序号(seq)为x,该报文段虽然不能携带数据.但要消耗掉一个序号.因此TCP客户进程发送的第二个报文段的序号为x+1.
        - TCP规定普通的TCP确认报文段可以携带数据,但如果不携带数据,则不消耗序号.
        - 如果该报文段不携带数据,则TCP客户进程要发送的下一个数据报文段的序号仍为x+1.
    - **确认号ack**字段的值被设置为y+1,这是对TCP服务器进程所选择的**初始号y**的确认
    - TCP服务器进程收到,针对TCP连接请求确认报文段的普通确认报文段后,也进入连接已建立状态.
    - 此时,TCP双方都进入了连接已建立状态,它们可以基于已建立的TCP连接进行可靠的数据

## 为什么使用三报文握手
![为什么使用三报文握手](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BD%BF%E7%94%A8%E4%B8%89%E6%8A%A5%E6%96%87%E6%8F%A1%E6%89%8B.png)

## 四次挥手过程

![四次挥手过程](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B.png)
- 假设TCP客户进程,主动关闭TCP连接,TCP客户进程会发送连接释放报文段并进入终止等待1状态
    - **TCP连接释放报文段**首部中的**终止标志位FIN**和**确认标志位ACK**的值都被设置为1.表明这是一个**TCP连接释放报文段**,同时也对之前收到的TCP报文段进行确认.
    - **序号seq**字段的值设置为u,它等于TCP客户进程之前已经传送过的数据的最后一个字节的序号加1
    - TCP规定**终止标志位FIN**等于1的TCP报文段即使不携带数据,也要消耗掉一个序号.
    - **确认号ack**字段的值设置为v,它等于TCP客户进程之前已收到的数据的最后一个字节的序号加1.
- TCP服务器进程收到**TCP连接释放报文段**后,会发送一个普通的TCP确认报文段并进入**关闭等待状态**.
    - 该报文段首部中的**确认标志位ACK**的值被设置为1,表明这是一个**TCP普通确认报文段**.
    - **序号seq**字段的值设置为v,它等于TCP服务器进程之前已传送过的数据的最后一个字节的序号加1.这也与之前收到的TCP连接释放报文段中的确认号v匹配.
    - **确认号ack**字段的值设置为u+1,这是对TCP连接释放报文段的确认.
    - TCP服务器进程这时应通知高层应用进程,TCP客户进程要断开与自己的TCP连接,**此时从TCP客户进程到TCP服务器进程这个方向的连接就释放了**,此时的TCP连接属于**半关闭状态**
        - TCP客户进程已经没有数据要发送了.但TCP服务器进程如果还有数据要发送,TCP客户进程仍要接收,也就是从TCP服务器进程到TCP客户进程这个方向的连接并未关闭
        - 半关闭状态可能会持续一段时间
- TCP客户进程收到该普通的TCP确认报文段后,就进入**终止等待2**状态,等待TCP服务器进程发出的**TCP连接释放报文段**.
    - 若使用TCP服务器的应用进程,已经没有数据要发送了,应用进程就通知其TCP服务器进程释放连接
- 由于TCP连接释放是由TCP客户进程主动发起的,因此TCP服务器进程对TCP连接的释放称为**被动关闭连接**.
    - TCP服务器进程发送**TCP连接释放报文段**并进入最后确认状态.
    - **TCP连接释放报文段**首部中的**终止标志位FIN**和**确认标志位ACK**的值都被设置为1.表明这是一个**TCP连接释放报文段**,同时也对之前收到的TCP报文段进行确认.
    - **序号seq**字段的值假定被设置为w,这是因为在**半关闭**状态下TCP服务器进程可能又发送了一些数据.
    - **确认号ack**字段的值被设置为u+1,这是对之前收到的**TCP连接释放报文段的重复确认**.
- TCP客户进程收到**TCP连接释放报文段**后,必须针对该报文段发送普通的TCP确认报文段并进入时间等待状态.
    - 该报文段首部中**确认标志位ACK**的值被设置为1,表明这是一个TCP普通确认报文段.
    - **序号seq**字段的值设置为u+1,这是因为TCP客户进程之前发送的**TCP连接释放报文段**虽然不携带数据,但要消耗掉一个序号
    - **确认号**ack字段的值设置为w+1,这是对所收到的**TCP连接释放报文段**的确认.
    - TCP服务器进行收到该普通的TCP确认报文段后,就进入关闭状态,服务器进程撤销相应的传输控制块.
- TCP客户进程还要经过**2MSL**后,才能进入关闭状态
    - MSL是**最长报文段寿命**(Maximun Segment Lifetime)的英文缩写词,[RFC793]建议为2分钟.也就是说,TCP客户进程进入时间等待(**TIME-WAIT**)状态后,还要经过4分钟才能进入关闭(CLOSED)状态.这完全是从工程上来考虑的.对于现在的网络,MSL取2分钟可能太长了,因此TCP允许不同的实现可根据具体情况使用更小的MSL值.
    - 经过2MSL时间后,客户进程撤销相应的传输控制块后,就结束了这次的TCP连接.

### [如何尽量处理TIME_WAIT过多?](https://www.cnblogs.com/dadonggg/p/8778318.html)
编辑内核文件/etc/sysctl.conf,加入以下内容:
```shell
net.ipv4.tcp_syncookies = 1 表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭；
net.ipv4.tcp_tw_reuse = 1 表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭；
net.ipv4.tcp_tw_recycle = 1 表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭。
net.ipv4.tcp_fin_timeout 修改系默认的 TIMEOUT 时间
```
然后执行 /sbin/sysctl -p 让参数生效.
简单来说，就是打开系统的TIMEWAIT重用和快速回收。

# 网络层
网络层的主要任务是**实现网络互连**,进而**实现数据包在各网络之间的传输**
要实现网络层任务,需要解决以下主要问题:
- 网络层向运输层提供怎样的服务(可靠传输还是不可靠传输)
- 网络层寻址问题
- 路由选择问题

## 网际控制报文协议ICMP
- 为了更有效地发送IP数据报(网际层)和提高交付成功的机会,在网际层使用了网际控制报文协议ICMP.
- 主机或路由器使用ICMP来发送**差错报告报文**和**询问报文**.
- **ICMP报文被封装在IP数据报**中发送.

ICMP差错报告报文共有以下五种:
- 终点不可达
    - 当路由器
- 源点抑制
- 时间超过
- 参数问题
- 改变路由(重定向)

## 网络适配器和MAC地址
### 网络适配器
![网络适配器](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E7%BD%91%E7%BB%9C%E9%80%82%E9%85%8D%E5%99%A8.png)
### 网络适配器
![网络适配器](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/%E7%BD%91%E7%BB%9C%E9%80%82%E9%85%8D%E5%99%A82.png)
### mac1
![mac1](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/mac%E5%9C%B0%E5%9D%801.png)
### mac2
![mac2](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/mac%E5%9C%B0%E5%9D%802.png)
### mac3
![mac3](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/mac%E5%9C%B0%E5%9D%803.png)
### mac4
![mac4](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/mac%E5%9C%B0%E5%9D%804.png)
### mac5
![mac5](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/mac%E5%9C%B0%E5%9D%805.png)
### mac地址6_单播mac地址
![mac地址6_单播mac地址.png](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/mac%E5%9C%B0%E5%9D%806_%E5%8D%95%E6%92%ADmac%E5%9C%B0%E5%9D%80.png)
### mac地址7_广播mac地址
![mac地址7_广播mac地址](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/mac%E5%9C%B0%E5%9D%807_%E5%B9%BF%E6%92%ADmac%E5%9C%B0%E5%9D%80.png)
### mac地址8_多播mac地址
![mac地址8_多播mac地址.png](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/mac%E5%9C%B0%E5%9D%808_%E5%A4%9A%E6%92%ADmac%E5%9C%B0%E5%9D%80.png)
### mac地址9_总结
![mac地址9_总结.png](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/network/mac%E5%9C%B0%E5%9D%809_%E6%80%BB%E7%BB%93.png)
