## 哈希

-   **Hash**: 一般翻译做“散列”，也有直接音译为“哈希”的，就是把任意长度的输入（又叫做预映射， pre-image），通过散列算法，变换成**固定长度的输出，该输出就是散列值**。这种转换是一种压缩映射，也就是，散列值的空间通常远小于输入的空间，不同的输入可能会散列成相同的输出，而不可能从散列值来唯一的确定输入值。简单的说就是**一种将任意长度的消息压缩到某一固定长度的消息摘要的函数。**
   
-   **哈希表又叫散列表**，是一种根据设定的映射函数f(key)将一组关键字映射到一个有限且连续的地址区间上，并以关键字在地址区间中的“像”作为元素在表中的存储位置的一种数据结构。这个映射过程称为**哈希造表**或者**散列**，这个映射函数f(key)即为**哈希函数**也叫**散列函数**，通过哈希函数得到的存储位置称为哈希地址或散列地址

-   **哈希（Hash）算法**: 即**散列函数**。它是一种单向密码体制，即它是一个**从明文到密文的不可逆的映射**，只有加密过程，没有解密过程。同时，哈希函数可以将任意长度的输入经过变化以后得到固定长度的输出。哈希函数的这种单向特征和输出数据长度固定的特征使得它可以生成消息或者数据。

-   **哈希碰撞**: 对于不同的关键字，可能得到同一个哈希地址，即key1≠key2,而 f(key1)=f(key2)，对于这种现象我们称之为**哈希冲突**，也叫**哈希碰撞**
    - 一般情况下，哈希冲突只能尽可能的减少，但不可能完全避免。因为哈希函数是从关键字集合到地址集合的映射，通常来说关键字集合比较大，它的元素理论上包括所有可能的关键字，而地址集合的元素仅为哈希表中的地址值。这就导致了哈希冲突的必然性。

-   **解决哈希冲突**:
    -   **开放地址法**:
    -   **再哈希法**
    -   **建立公共溢出区**
    -   **链地址法**

-   **静态哈希**:
    -   **开放寻址法(开放地址法)**:性能上依然碾压一切,当发生地址冲突时，按照某种方法继续探测哈希表中的其他存储单元，直到找到空位置为止.
    -   **多重哈希法(再哈希法)**:在产生哈希冲突的时候计算另一个哈希函数，直到不再发生冲突为止.
    -   **拉链法(链地址法)**: 链地址法是指在碰到哈希冲突的时候，将冲突的元素以链表的形式进行存储.
    -   **常见的哈希函数的实现**:
        - CRC-64: 用于网络数据包错误检测
        - NurmurHash: 快速通用的
        - Google CityHash:短key快速的
        - Facebook XXHash:来自zstd压缩的创作者
        - Google FarmHash: 新版本的City Hash, 具有更好的哈希碰撞率

- **动态哈希**
    - **多哈希表**: 采用多个哈希表来扩展原来的哈希表,多个哈希表公用一个哈希函数.质量达不到数量凑
        - 桶满时触发新的哈希表创建


## 分布式ID

1.  全局唯一性
    *   不能出现重复的ID标识
2.  趋势递增
    *   在MySQL InnoDB引擎中使用的是聚集索引，由于多数RDBMS使用B-tree的数据结构来存储索引数据，在主键的选择上面我们应该尽量使用有序的主键保证写入性能。
3.  单调递增
    *   保证下一个ID一定大于上一个ID，例如事务版本号、IM增量消息、排序等特殊需求。
4.  信息安全
    *   如果ID是连续的，恶意用户的扒取工作就非常容易做了，直接按照顺序下载指定URL即可；如果是订单号就更危险了，竞对可以直接知道我们一天的单量。所以在一些应用场景下，会需要ID无规则、不规则。

上述123对应三类不同的场景，3和4需求还是互斥的，无法使用同一个方案满足。

### 1雪花算法

![image](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/devops/concurrencyControl/%E9%9B%AA%E8%8A%B1%E7%AE%97%E6%B3%95.jpg)

*   莱布尼茨:世界上没有相同的两片叶子,雪花由10^19个水分子组成,自然界不存在完全一样的雪花
*   snowflake是Twitter开源的**分布式ID生成算法**
*   一共64bit
    1.  **第一位**: 占用1bit,始终是0,没有实际作用.
    2.  **时间戳**: 占用41bit,精确到毫秒,总共可以容纳约69年的时间.
    3.  **工作机器id**: 占用10bit,其中高位5bit是数据中心ID,地位5bit是工作节点ID,最多可容纳1024个节点.
    4.  **序列号**: 占用12bit,每个节点每毫秒从0开始不断累加,最多可以累加到4095,一共产生4096个ID.
*   SnowFlake算法在同一毫秒内产生的全局唯一ID数量: 1024\*4096=4194304

## B+树
- B+树: 特性决定支持范围查找和模糊匹配.相对于Hash表而言,B+树无需通过一个具体的Key来查找.
    - 通常Key和Value是分离的,因为便于利用CPU的缓存特性.
    - 通常节点中有两个指针指向相邻的兄弟节点.
    - B+树可以根据层数估算存储的数据量: **((Page大小-元数据大小)/元祖大小)^层数**
    - 实际系统中需要将元祖中的那个数据作为RecordID?
        - 指向索引项对应的元组位置的指针
        - 元组的实际内容存储在叶子节点中,二级索引必须将RecordID存储为其值.
    - B+ 树与 B 树相比, B+ 树只能将Value存储到叶子节点.
    - 可以在多个列上定义复合索引,**定义顺序影响查找方式**
    - 变长字段作为索引键的时候PostgreSQL会使用null或者0填充进行对齐.
    - 如果插入的数据超过varchar的长度,MySQL会默默地切掉后边的数据,而PostgreSQL会给出错误.
    - **Sorted Key Map**是一种微优化,在内存中处理,将B+树中的节点中的每个元组前一个字符提取出来使用数组保存,这样查询对比时,**如果第一个字符就不相等,那么可以直接跳过**, 这样可以避免加载很多数据导致缓存失败.
    - B+树上重复的Key如何处理?
        - 插入RecordID
        - 使用溢出叶节点进行垂直扩展
- 聚簇索引: **让数据按照某种方式进行排序,例如主键**.数据库系统会保证索引对Page中的元组的物理布局进行重新组织.
    - 如果没有定义主键,MySQL会自动定义一个,对我们是透明的
    - PostgreSQL并不会按照主键的顺序来排序,因为主键是聚簇索引的排序方式.
    - 也叫聚集索引,缺点在于更新的代价高,因为需要将数据移动到指定的位置.插入速度严重依赖于插入顺序.更新时可能导致页分裂问题.聚集索引也可能会导致全表扫描速度变慢,因为逻辑上连续的页在物理上可能相隔较远,产生大量的随机IO.
    - 覆盖索引: 查询的字段都是索引的字段
    - 优化: 让B+树变得更快
        - 前缀压缩: 多个排序的Key具有相同的前缀可以进行压缩,**使用Trie树**.
        - 后缀截断: 使用**指定长度的字符串**就可以判断不同的Key,那么后边没用的截掉就可以了.
        - 批量插入: 例如批量加载一个数据集,这样就会提前拥有全部的Key,可以**先进行排序后再批量插入**
        - 指针混用: 使用B+树中的PageID替换为缓冲池中的指针
    - 函数/表达式索引: 用户不想通过Key来查找记录,而是某种方法
    - Trie树/基数树

## 进程模型
- 每个进程负责一个Worker,DB2,Orache和PostgreSQL使用这种方式.
    - 使用共享内存实现BUffer Pool共享,避免多个进程加载不同的Page
    - 如果一个进程崩溃了不会影响另一个Worker
- 每个线程负责一个Worker,Mysql实现了该模型,现代数据库相同一般会使用该模型
- 进程池/线程池,DB2和PostgreSQL实现了该模型
    - 一些高端的数据库可能会实现工作机制

>工作窃取（work-stealing）算法是指某个线程从其他队列里窃取任务来执行。那么，为什么需要使用工作窃取算法呢？假如我们需要做一个比较大的任务，可以把这个任务分割为若干互不依赖的子任务，为了减少线程间的竞争，把这些子任务分别放到不同的队列里，并为每个队列创建一个单独的线程来执行队列里的任务，线程和队列一一对应。比如A线程负责处理A队列里的任务。但是，有的线程会先把自己队列里的任务干完，而其他线程对应的队列里还有任务等待处理。干完活的线程与其等着，不如去帮其他线程干活，于是它就去其他线程的队列里窃取一个任务来执行。而在这时它们会访问同一个队列，所以为了减少窃取任务线程和被窃取任务线程之间的竞争，通常会使用双端队列，被窃取任务线程永远从双端队列的头部拿任务执行，而窃取任务的线程永远从双端队列的尾部拿任务执行。
工作窃取的运行流程
![image](https://assetsasda.oss-cn-guangzhou.aliyuncs.com/devops/%E5%B7%A5%E4%BD%9C%E7%AA%83%E5%8F%96%E7%AE%97%E6%B3%95.png)
工作窃取算法的优点：充分利用线程进行并行计算，减少了线程间的竞争。
工作窃取算法的缺点：在某些情况下还是存在竞争，比如双端队列里只有一个任务时。并且该算法会消耗了更多的系统资源，比如创建多个线程和多个双端队列。

## 并发控制

- BASE理论: BA指的是 **基本业务可用性,支持分区失败**,S表示柔性状态,也就是**允许短时间内不同步**,E表示最终一致性,**数据最终是一致的**.原子性和持久性必须从根本上保障,为了可用性、性能和服务降级的需要,只有降低一致性和隔离性的要求.
    - 不符合ACID的系统通常以BASE冠名.BASE唯一可以做的事情就是不承认ACID,此外没有任何保障
- CAP定理:对于共享数据系统,最多只能同时拥有CAP其中的两个,任意两个都有其适应的场景,真实的业务系统中通常是ACID与CAP的混合体.分布式系统中最重要的是满足业务需求,而不是追求高度抽象,绝对的系统特性.
    - C表示**一致性**,也就是所有用户看到的数据是一样的.CAP只是使用一致性来标识线性化.
    - A表示**可用性**,是指总能找到一个可用的数据副本
    - P表示**分区容错性**,能够容忍网路中断等故障
- 数据并发问题,针对事务的隔离性和并发性,怎么做取舍?
    - 脏写(Dirty Write):对于两个事务Session A,Session B,如果事务SessionA`修改了`另一个`未提交`事务Session B`修改过`的数据,那就意味着发生了`脏写`
    - **脏读(Dirty Read)**:读到了别的事务回滚前的脏数据,对于两个事务Session A和Session B,Session A`读取`了已被Session B`更新`但还`没有提交`的字段.之后若Session B`回滚`,Session A `读取`的内容就是`临时且无效的`.
    - **不可重复读(Non-Repeatable Read)**:对于两个事务Session A、Session B,Session A `读取`了一个字段,然后 Session B `更新`了该字段. 之后Session A 再次读取同一个字段, 值就不同了.那就意味着发生了不可重复读.
    - **幻读(Phantom)**: 对于两个事务Session A、Session B, Session A 从一个表中`读取`了一个字段, 然后 Session B 在该表中`插入`了一些新的行。 之后, 如果 Session A `再次读取`同一个表, 就会多出几行。那就意味着发生了幻读。
- 事务: 一组逻辑操作单元，使数据从一种状态变换到另一种状态。
    - 事务的实现方式:
        - 使用**重做日志**保证原子性
        - 使用**影子分页**保证原子性,使用指针指向新的Page副本.是System R发明的,现在CouchDB和LMDB(OpenLDAP)在使用.
        - 原子性: 银行转账的例子
    - **一致性**: 根据定义，一致性是指事务执行前后，数据从一个合法性状态变换到另外一个合法性状态。这种状态是语义上的而不是语法上的，跟具体的业务有关。那什么是合法的数据状态呢？满足预定的约束的状态就叫做合法的状态。通俗一点，这状态是由你自己来定义的（比如满足现实世界中的约束）。满足这个状态，数据就是一致的，不满足这个状态，数据就是不一致的！如果事务中的某个操作失败了，系统就会自动撤销当前正在执行的事务，返回到事务操作之前的状态。
        - 数据库的完整性约束没有被破坏,一般会通过重做日志实现
        - MySQL的重做日志分为Redo和Undo,**Redo具有内存缓冲区**,Redo保证事务的持久性,是顺序写的.
        - Undo用来实现事务回滚和MVCC
        - 数据库系统的一致性与分布式系统的一致性:
            - 数据库的一致性在于ACID的一致性,也就是关乎操作的一致性,分布式系统的一致性更加注重数据的一致性
            - 数据库的一致性核心在于约束,约束是由数据库的使用者告诉数据库系统的
            - 外部一致性的核心是并发控制,实现外部一致性的核心是可串行化和可线性化
            - 数据库系统存在事务的并发控制问题,并且ACID的隔离性受到并发控制的影响
    - **隔离性**:事务的隔离性是指一个事务的执行**不能被其他事务干扰**，即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，**并发**执行的各个事务之间不能互相干扰。
        - 也叫并发控制,本质是假装并发没有发生
        - SQL标准定义的**四个隔离级别**:
            - **读未提交(READ UNCOMMITTED)**:读未提交，在该隔离级别，所有事务都可以看到其他未提交事务的执行结果。不能避免脏读、不可重复读、幻读。
            - **读已提交(READ COMMITTED)**: 只能读取其它事务修改并已经提交的数据.避免了**脏读**,但是不能避免**幻读**和**不可重复读**.读已提交是大多数主流数据库的默认事务等级.
                - 读数据库时,事务只能看到已经提交成功的数据,避免了脏读
                - 写数据库时,事务只能看到已经提交成功的数据,避免了脏写.数据库通常使用行级锁实现.
            - **可重复读(REPEATABLE READ)**:可重复读，事务A在读到一条数据之后，此时事务B对该数据进行了修改并提交，那么事务A再读该数据，读到的还是原来的内容。可以避免脏读、不可重复读，但幻读问题仍然存在。这是MySQL的默认隔离级别。
                - Oracle称为可串行化,PostgreSQL和Mysql称为可重复读
            - **可串行化(SERIALIZABLE)**: 读取前锁定所有要读取的数据,当前事务提交前,其它事务不允许修改.最严格的级别,事务串行执行,资源消耗最大
                - 解决并发问题的最直接原因是避免并发,在一个线程上顺序执行事务,但是这是在2007年才被认可
                    - 内存变得便宜
                    - OLTP事务通常很快且以读为主
                - 数据库系统的可串行化和分布式系统的可线行化:
                    - 可串行化保证的是编程模型中的一些约束,这些约束是人为规定的
                    - 可线性化保证的是分布式系统中操作与操作产生的记录确定是一致的,那么就称为可线性化的.
    - **持久性**: 持久性是指一个事务一旦被提交，它对数据库中数据的改变就是**永久性的**，接下来的其他操作和数据库故障不应该对其有任何影响。
    - **原子性**: 原子性是指事务是一个不可分割的工作单位,要么全部提交,要么全部失败回滚.

| 隔离级别 | 脏读可能性 | 不可重复读可能性 | 幻读可能性 | 加锁读 |
| --- | --- | --- | --- | --- |
| 读未提交(READ UNCOMMITTED) | Yes | Yes | Yes | No |
| 读已提交(READ COMMITTED) | No | Yes | Yes | No |
| 可重复读(REPEATABLE READ) | No | No | Yes | No |
| 可串行化(SERIALIZABLE) | No | No | No | Yes |

- 事务的分类
    - 扁平事务: 最常见的事务,所有的操作都处于同一层次
        - **带保存点的扁平事务**: 允许在事务执行过程中回滚到同一事物的较早状态.当系统发生崩溃时,所有的保存点会丢失,然后需要进行整个事务的重新执行.
    - 链事务: 保存点的一个变种,提交一个事务时,释放不需要的数据对象,将必要的处理上下文隐式的传递给下一个要开始的事务.
        - **带有保存点的事务可以回滚到任意保存点,链事务不行.**
    - 嵌套事务: 顶层事务下面有许多子事务,是一棵树.
    - 分布式事务: 在分布式环境下运行的扁平事务.允许多个独立的事务资源参与到一个全局的事务中.
    
## 业务系统上的事务支持
- 本地事务: 当事务**由资源管理器本地管理时**被称作本地事务
    - 本地事务的优点就是**支持严格的ACID特性**,高效,可靠,状态可以只在资源管理器中维护,而且应用编程模型简单.
    - 本地事务不具备分布式事务的处理能力,**隔离的最小单位受限于资源管理器**.
- 全局事务: 当事务**由全局事务管理器进行全局管理时**成为全局事务.事务管理器负责管理全局的事务状态和参与的资源,协同资源的一致提交回滚.
- TX协议: 应用或者应用服务器与事务管理器的接口.
- XA协议: **全局事务管理器与资源管理器的接口**.XA是由X/Open组织提出的分布式事务规范.该规范主要定义了全局事务管理器和局部资源管理器之间的接口.主流的数据库产品都实现了XA接口.XA接口是一个双向的系统接口,在事务管理器以及多个资源管理器之间作为通信桥梁.之所以需要XA是因为在分布式系统中从理论上将两台机器是无法达到一致状态的,因此引入一个单点进行协调.由全局事务管理器管理和协调的事务可以跨越多个资源和进程.全局事务管理器一般使用XA二阶段协议与数据库进行交互.
- AP:应用程序,可以理解为使用DTP(Data Tools Platform)的程序.
- RM: 资源管理器,这里可以是一个DBMS或者消息服务器管理系统,应用程序通过资源管理器对资源进行控制,资源必须实现XA定义的接口.资源管理器负责控制和管理实际的资源.
- TM: 事务管理器,负责协调和管理事务,使用给AP编程接口以及管理资源管理器.事务管理器控制着全局事务,管理事务的生命周期,并且协调资源.
- 2PC(两阶段提交协议): XA用于在全局事务中协调多个资源的机制.TM和RM之间采取两阶段提交的方案来解决一致性问题.两节点提交需要一个协调者(TM)来掌控所有参与者(RM)节点的操作结果并且指引这些节点是否需要最终提交.说白了就是引入协调者这个角色保证数据的强一致性.
    - 两阶段提交的局限在于协议成本,准备阶段的持久成本,全局事务状态的持久成本,潜在故障点多带来的脆弱性,准备后,提交前的故障引发一系列隔离与恢复难题.
    - 缺点: 参与的节点都是同步阻塞的,协调者存在单点故障,Commit时协调者故障导致数据不一致.
- 3PC(三阶段提交协议): 将提交事务请求的过程分为canCommit和preCommit两个过程.
    - preCommit可能的情况为执行事务提前进入doCommit阶段和中断事务.
    - 进入doCommit之后可能存在协调者出现问题或者网络问题,这样只能设计一个超时机制.
    - 优点: 降低了2PC参与者的阻塞范围,单点故障后继续可以达成一致
    - 缺点: 参与者接收到preCommit消息之后,如果出现网络分区,此时事务依然会提交,这种情况下出现不一致.
- 业务系统中柔性事务的服务模式
    - 可查询操作: 服务操作具有全局唯一的标识,操作唯一的确定的时间.
    - 幂等操作: 重复调用多次产生的业务结果与调用一次产生的结果相同.一是通过业务操作实现幂等性,二是系统缓存所有请求与处理的结果,最后是检测到重复请求之后,自动返回之前的处理结果.
    - TCC操作:
        - Try阶段,尝试执行业务,完成所有业务的检查,实现一致性;预留必须的业务资源,实现准隔离性.
        - COnfirm阶段: 真正的去执行业务,不做任何检查,仅适合用Try阶段预留的业务资源,Confirm操作还要满足幂等性.
        - Cancel阶段: 取消执行业务,释放Try阶段预留的业务资源,Cancel操作要满足幂等性.
        - TCC与2PC(两阶段提交)协议的区别:
            - TCC位于业务服务层而不是资源层,TCC没有单独准备阶段,Try操作兼备资源操作与准备的能力.
            - TCC中Try操作可以灵活的选择业务资源,锁定粒度.
            - TCC的开发成本比2PC高.实际上TCC也属于两阶段操作,但是TCC不等同于2PC操作.
        - TCC对业务服务代码侵入较高,维护成本也随之上去了.try/confirm/cancel必须实现幂等性.事务管理器的实现需要日志,拉长了TCC整个过程.
    - 可补偿操作:
        - Do阶段: 真正的执行业务处理,业务处理结果外部可见.
        - Compensate阶段: 抵消或者部分撤销正向业务操作的业务结果,补偿操作满足幂等性.
            - 约束: 补偿操作在业务上可行,由于业务执行结果未隔离或者补偿不完整带来的风险与成本可控.实际上,TCC的Confirm和Cancel操作可以看做是补偿操作.
    - Saga操作: Saga在1987年提出,由一系列本地事务构成,从架构上讲分为中心化的(基于事件)和去中心化的(基于命令).
        - 事件模式: 一个本地事务执行完成之后发出命令,挂载该事件的本地事务事务执行,回滚的实现需要业务提供补偿接口.但是参与的业务方较多的时候会导致失控.大家随意挂载事件,还可能引发环形事件.
        - 命令模式: 定义一个与业务无关的服务作为事务的协调者.解决了事件模式的缺点带来的问题是需要维护一个协调中心.














